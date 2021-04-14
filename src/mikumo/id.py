import json
import requests

from . import MY_CONSTANT

ENDPOINT = ''

#def get_token_and_endpoint(access, service)
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

def get_access(credentials):
    username = credentials['user']
    password = credentials['pass']
    tenant = '0'
    endpoint = credentials['id']['endpoint']

    payload = {'auth': {'passwordCredentials': {'username': username, 'password': password}, 'tenantId': tenant}}
    res = requests.post(endpoint + '/tokens', data = json.dumps(payload))
    d = res.json()
    d['id-endpoint'] = endpoint
    print(d)

    return res.status_code, d

def hi():
    print('hi, world')
