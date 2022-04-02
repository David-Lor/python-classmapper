from classmapper import ClassMapper


class FromClass:
    def __init__(self, identifier, name, age):
        self.identifier = identifier
        self.name = name
        self.age = age


class ToClass:
    def __init__(self, _id, name):
        self._id = _id
        self.name = name


def test_mapper_simple_decorator():
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

    @mapper.register(FromClass, ToClass)
    def mapper_func(_from: FromClass):
        return ToClass(
            _id=_from.identifier,
            name=_from.name
        )

    r = mapper.map(from_instance, ToClass)
    assert r.__dict__ == expected_to_instance.__dict__
