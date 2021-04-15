# Identity API v2.0

import json
import requests

def get_version_list(access):
    """
    バージョン情報取得
    https://www.conoha.jp/docs/identity-get_version_list.php
    """
    endpoint = access['id-endpoint']

    res = requests.get(endpoint + '/')

    return res.status_code, res.json()

def get_version_detail(access):
    """
    バージョン情報詳細取得
    https://www.conoha.jp/docs/identity-get_version_detail.php
    """
    endpoint = access['id-endpoint']

    res = requests.get(endpoint + '/v2.0')

    return res.status_code, res.json()

def post_tokens(credentials):
    """
    トークン発行
    https://www.conoha.jp/docs/identity-post_tokens.php
    """
    username  = credentials['user']
    password  = credentials['pass']
    tenant_id = credentials['tenant-id']
    endpoint  = credentials['identity-endpoint']

    payload = {'auth': {'passwordCredentials':
            {'username': username, 'password': password}, 'tenantId': tenant_id}}
    res = requests.post(endpoint + '/tokens', data = json.dumps(payload))
    d = res.json()
    d['id-endpoint'] = endpoint

    return res.status_code, d

def get_token_and_endpoint(access, type):
    token = access['access']['token']['id']

    for service in access['access']['serviceCatalog']:
        if service['type'] == type:
            endpoint = service['endpoints'][0]['publicURL']

    print('token:', token)
    print('endpoint:', endpoint)
    return token, endpoint

def set_endpoint(endpoint):
    global ENDPOINT
    ENDPOINT = endpoint


def hi():
    print('hi, world')
