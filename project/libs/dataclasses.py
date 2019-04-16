from dataclasses import asdict, astuple, dataclass as base_dataclass, replace

__all__ = ["dataclass"]


def dataclass(
    _cls=None, *, frozen=True, order=True, sort_errors=True, **kwargs
):
    def wrap(cls):
        setattr(cls, cls_asdict.__name__, cls_asdict)
        setattr(cls, cls_astuple.__name__, cls_astuple)
        setattr(cls, cls_replace.__name__, cls_replace)

        return base_dataclass(cls, frozen=frozen, order=order, **kwargs)

    if _cls is None:
        return wrap

    return wrap(_cls)


def cls_asdict(self):
    return asdict(self)


def cls_astuple(self):
    return astuple(self)


def cls_replace(self, **changes):
    return replace(self, **changes)


cls_asdict.__name__ = "asdict"
cls_asdict.__qualname__ = "asdict"
cls_astuple.__name__ = "astuple"
cls_astuple.__qualname__ = "astuple"
cls_replace.__name__ = "replace"
cls_replace.__qualname__ = "replace"
