from dataclasses import dataclass
from typing import TypeVar


@dataclass
class Point:
    x: int
    y: int


T = TypeVar('T')
U = TypeVar('U')


def swap(x: T, y: U) -> tuple[U, T]:
    return (y, x)


print(Point.__annotations__)
print(swap.__annotations__)

# print(repr(Point.__annotations__['x']()))
