# Python ClassMapper

A simple class mapping (conversion) Python library.

## Example

Imagine you have two classes, `OriginCls` and `DestinationCls`:

```python
from dataclasses import dataclass

@dataclass
class OriginCls:
    id: str
    name: str
    age: int

@dataclass
class DestinationCls:
    _id: str
    data: dict
```

You want to be able to convert an object of `OriginCls` to `DestinationCls` and viceversa.
ClassMapper allows you to define "mappers" - functions that explicitly convert an object of a class A to a new instance of a class B.
Being explicit means that you have to explicitly define how the conversion between classes is performed.

```python
from classmapper import ClassMapper

mapper = ClassMapper()

@mapper.register(OriginCls, DestinationCls)
def _mapper_origin_destination(_from: OriginCls) -> DestinationCls:
    return DestinationCls(
        _id=_from.id,
        data={
            "name": _from.name,
            "age": _from.age
        }
    )

@mapper.register(DestinationCls, OriginCls)
def _mapper_destination_origin(_from: DestinationCls) -> OriginCls:
    return OriginCls(
        id=_from._id,
        name=_from.data["name"],
        age=_from.data["age"]
    )
```

Now you can convert an object of `OriginCls` into `DestinationCls`, and viceversa:

```python
source = OriginCls(id="1", name="foo", age=21)
# mapper.map(source object, target class)
#   returns object of target class, if a mapper between source object's class and target class is registered
result = mapper.map(source, DestinationCls)
print(result)

# convert back into the original
result = mapper.map(result, OriginCls)
print(result)
```

If you try to convert between classes not mapped, a NoClassMappingError is raised:

```python
class OtherCls:
    pass

mapper.map(source, OtherCls)  # raises NoClassMappingError
```

More examples can be found on [tests](tests).
