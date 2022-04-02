from typing import Type

__all__ = ("BaseClassMapperException", "NoClassMappingError")


class BaseClassMapperException(Exception):
    pass


class NoClassMappingError(BaseClassMapperException):
    def __init__(self, from_obj, to_cls: Type):
        self.from_obj = from_obj
        self.to_cls = to_cls

    def __str__(self):
        return f"No class mapping defined from {self.from_obj.__class__.__name__} to {self.to_cls.__name__}"
