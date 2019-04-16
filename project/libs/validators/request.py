from functools import wraps

from project.libs.dataclasses import asdict
from project.libs.response import ErrorTypes, FieldError, ItemResp, Status


def serialize_errors(data, prefix=""):
    errors = []
    if prefix:
        prefix = prefix + "."

    for key, value in data.items():
        if isinstance(value, dict):
            key = str(key)
            errors.update(serialize_errors(value, prefix=prefix + key))
        else:
            field_name = prefix + key
            for error in value:
                if error == "Field may not be null.":
                    error = FieldError(
                        field=field_name,
                        type=ErrorTypes.required,
                        msg="Required field",
                    )
                else:
                    error = FieldError(
                        field=field_name,
                        type=ErrorTypes.invalid,
                        msg=error.rstrip("."),
                    )

                errors.append(error)

    return errors


def validate(req, schema, many=False):
    data = req
    if not isinstance(data, dict):
        data = asdict(req)
    schema = schema(data=data, many=many)

    if not schema.is_valid():
        errors = serialize_errors(schema.errors)
        return ItemResp(status=Status.invalid, errors=errors)

    req = schema.save()

    return ItemResp(item=req)


def validate_request(*args, schema=None, many=False):
    def wrapper(func):
        @wraps(func)
        def decorator(self, *args, **kwargs):
            req = args[0]
            result = validate(req, schema=schema, many=many)
            if not result.ok:
                return result
            args = [result.item, *args[1:]]
            return func(self, *args, **kwargs)

        return decorator

    if len(args) >= 1:
        func = args[0]
        return wrapper(func)

    return wrapper
