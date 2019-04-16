from enum import Enum
from http import HTTPStatus
from typing import List

from rest_framework.response import Response

from project.libs.dataclasses import dataclass


class Status(Enum):
    ok = 0
    not_found = 1
    not_ready = 2
    invalid = 3
    duplicated = 4
    unauthenticated = 5
    forbidden = 6
    conflict = 7


HTTP_STATUS_MAP = {
    Status.ok: HTTPStatus.OK,
    Status.not_found: HTTPStatus.NOT_FOUND,
    Status.invalid: HTTPStatus.BAD_REQUEST,
    Status.duplicated: HTTPStatus.CONFLICT,
    Status.conflict: HTTPStatus.CONFLICT,
    Status.unauthenticated: HTTPStatus.UNAUTHORIZED,
    Status.forbidden: HTTPStatus.FORBIDDEN,
}


class ErrorTypes(Enum):
    invalid = 0
    duplicated = 1
    required = 2
    not_found = 3
    rule = 4


HTTP_ERROR_MAP = {
    ErrorTypes.invalid: "invalid",
    ErrorTypes.duplicated: "duplicated",
    ErrorTypes.required: "required",
    ErrorTypes.not_found: "not_found",
    ErrorTypes.rule: "rule",
}


@dataclass
class FieldError:
    field: str
    type: ErrorTypes
    msg: str = ""


@dataclass
class BaseResp:
    status: Status = Status.ok
    errors: List[FieldError] = None

    @property
    def ok(self):
        return self.status == Status.ok

    def __post_init__(self):
        if self.errors:
            self.errors.sort()


@dataclass
class ItemResp(BaseResp):
    item: object = None

    @property
    def ok(self):
        return self.status == Status.ok

    def __post_init__(self):
        if self.errors:
            self.errors.sort()


@dataclass
class ItemsResp(BaseResp):
    items: List[object] = None


@dataclass
class PageResp(ItemsResp):
    items: List[object] = None
    page: int = None
    total: int = None


def dump_errors(errors):
    if not errors:
        return ""

    errors_data = []
    for error in errors:
        data = {
            "field": error.field,
            "type": HTTP_ERROR_MAP[error.type],
            "msg": "",
        }
        if error.msg:
            data["msg"] = error.msg

        errors_data.append(data)

    return {"errors": errors_data}


def http_status(status):
    return HTTP_STATUS_MAP.get(status, HTTPStatus.INTERNAL_SERVER_ERROR)


def django_to_reponse(resp: [ItemResp, ItemsResp, PageResp], schema):

    data = None
    status = http_status(resp.status)

    if resp.ok:
        if isinstance(resp, ItemResp):
            data = schema(resp.item).data
        elif isinstance(resp, ItemsResp):
            data = schema(resp.items).data
        elif isinstance(resp, PageResp):
            items = schema(resp.items)
            data = {
                "items": items,
                "page": resp.page,
                "total": resp.total
            }
    elif resp.errors:
        data = dump_errors(resp.errors)
        
    return Response(
        status=status,
        data=data
    )
