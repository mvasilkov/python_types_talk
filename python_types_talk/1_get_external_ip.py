import requests


def get_external_ip():
    response = requests.get('https://myip.wtf/json')
    return parse_response(response)


def parse_response(response):
    obj = response.json()
    return obj.get('YourFuckingIPAddress', 'Could not get IP')


# def parse_response(response: requests.Response):
#     obj = response.json()
#     return obj.get('YourFuckingIPAddress', 'Could not get IP')


if __name__ == '__main__':
    print(get_external_ip())
