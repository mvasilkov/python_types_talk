from typing import TypeVar

T = TypeVar('T')
U = TypeVar('U')


def swap(x: T, y: U) -> tuple[U, T]:
    return (y, x)


if __name__ == '__main__':
    a = swap(4, 'hello')

    a[0]
    a[1]
