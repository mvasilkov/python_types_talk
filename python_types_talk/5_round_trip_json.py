from typing import Literal

from pydantic import BaseModel


class Cat(BaseModel):
    name: str


class Dog(BaseModel):
    name: str


class Person(BaseModel):
    name: str
    pets: list[Cat | Dog]


# class Cat(BaseModel):
#     type: Literal['cat'] = 'cat'
#     name: str


# class Dog(BaseModel):
#     type: Literal['dog'] = 'dog'
#     name: str


if __name__ == '__main__':
    john = Person(
        name='John',
        pets=[
            Cat(name='Garfield'),
            Dog(name='Odie'),
        ],
    )

    john_json = john.json()
    print(john_json)

    loaded_john = Person.parse_raw(john_json)
    print(loaded_john)
