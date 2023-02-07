from typing import TypedDict


def check_port(port: int):
    print(f'Checking port {port}...')
    ...


def connect(options: dict):
    print('host: ' + options['host'])
    print('port: ' + options['port'])

    check_port(options['port'])


# class OptionsDict(TypedDict):
#     host: str
#     port: int | None


# def connect(options: OptionsDict):
#     print('host: ' + options['host'])
#     print('port: ' + options['port'])

#     check_port(options['port'])


if __name__ == '__main__':
    connect({'host': 'localhost', 'port': '8000'})
    connect({'host': 'localhost', 'port': 9000})
