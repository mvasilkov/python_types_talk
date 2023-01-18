from typing import Literal


def setup_prevention(prevention_type):
    print('Setting up prevention: ' + prevention_type)
    ...


# def setup_prevention(prevention_type: str):
#     print('Setting up prevention: ' + prevention_type)
#     ...


# def setup_prevention(prevention_type: Literal['azure', 'layer7', 'nginx']):
#     print('Setting up prevention: ' + prevention_type)
#     ...


if __name__ == '__main__':
    setup_prevention(3)
    setup_prevention('azure')
    setup_prevention('layer7')
    setup_prevention('nginks')
