import pytest

from classmapper import ClassMapper, NoClassMappingError


class FromClass:
    def __init__(self, identifier, name, age):
        self.identifier = identifier
        self.name = name
        self.age = age


class ToClass:
    def __init__(self, _id, name):
        self._id = _id
        self.name = name


def mapper_func(_from: FromClass):
    return ToClass(
        _id=_from.identifier,
        name=_from.name
    )


def test_mapper_simple():
    from_instance = FromClass(
        identifier="#1",
        name="foo",
        age="25"
    )
    expected_to_instance = ToClass(
        _id=from_instance.identifier,
        name=from_instance.name,
    )

    mapper = ClassMapper()
    mapper.register_mapper(FromClass, ToClass, mapper_func)

    r = mapper.map(from_instance, ToClass)
    assert r.__dict__ == expected_to_instance.__dict__


def test_mapper_not_configured():
    from_instance = FromClass(
        identifier="#1",
        name="foo",
        age="25"
    )

    mapper = ClassMapper()
    exception = None
    with pytest.raises(NoClassMappingError):
        try:
            mapper.map(from_instance, ToClass)
        except Exception as ex:
            exception = ex
            raise ex

    assert str(exception) == "No class mapping defined from FromClass to ToClass"
