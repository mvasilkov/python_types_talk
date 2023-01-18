import json
from typing import TypeVar

T = TypeVar('T')


def check_value(value):
    print(f'Checking value {value}...')
    ...
    result = json.loads(json.dumps(value))
    return result


# def check_value(value: T) -> T:
#     print(f'Checking value {value}...')
#     ...
#     result = json.loads(json.dumps(value))
#     return result


a = check_value(4)
b = check_value('hello')
c = check_value([1, 2, 3])
