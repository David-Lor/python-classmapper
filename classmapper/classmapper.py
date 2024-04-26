from typing import Dict, Tuple, Type, Protocol, Any

from .exceptions import NoClassMappingError

__all__ = ("ClassMapper", "MapperFunc")


class MapperFunc(Protocol):
    # TODO Typing for **kwargs not working fine when specifying custom arguments (see test typing warning)
    def __call__(self, _from, **kwargs: Any) -> Any: ...


class ClassMapper:
    def __init__(self):
        self._mappers: Dict[Tuple[Type, Type], MapperFunc] = dict()

    def map(self, _from, _to_cls: Type, **kwargs) -> Any:
        """Map an object "_from" to an instance of the class "_to_cls",
        considering the types of "_from" and "_to_cls" are already configured on the mapper."""
        try:
            func = self._mappers[(_from.__class__, _to_cls)]
        except KeyError:
            raise NoClassMappingError(_from, _to_cls)

        return func(_from, **kwargs)

    def register_mapper(self, from_cls: Type, to_cls: Type, func: MapperFunc):
        self._mappers[(from_cls, to_cls)] = func

    def register(self, from_cls: Type, to_cls: Type):
        def decorator(func):
            self.register_mapper(from_cls, to_cls, func)
        return decorator
