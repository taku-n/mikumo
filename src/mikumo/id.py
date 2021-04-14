import requests

from . import MY_CONSTANT

ENDPOINT = ''

def set_endpoint(endpoint):
    global ENDPOINT
    ENDPOINT = endpoint

def ver():
    global ENDPOINT
    print('ENDPOINT:', ENDPOINT)
    res = requests.get(ENDPOINT + '/')
    print(res.status_code)
    print(res.json())
    print(MY_CONSTANT)

def hi():
    print('hi, world')
