# Identity API v2.0

import json
import requests

def get_version(access):
    """
    バージョン情報取得  
    https://www.conoha.jp/docs/identity-get_version_list.php
    """
    endpoint = access['identity-endpoint'][:-5]  # remove /v2.0

    res = requests.get(endpoint + '/')

    return res.status_code, res.json()

def get_version_in_detail(access):
    """
    バージョン情報詳細取得  
    https://www.conoha.jp/docs/identity-get_version_detail.php
    """
    endpoint = access['identity-endpoint']

    res = requests.get(endpoint + '/')

    return res.status_code, res.json()

def get_access(credentials):
    """
    トークン発行  
    https://www.conoha.jp/docs/identity-post_tokens.php
    """
    username  = credentials['api-username']
    password  = credentials['api-password']
    tenant_id = credentials['tenant-id']
    endpoint  = credentials['identity-endpoint']

    payload = {'auth': {'passwordCredentials':
            {'username': username, 'password': password}, 'tenantId': tenant_id}}
    res = requests.post(endpoint + '/tokens', data = json.dumps(payload))
    access = res.json()
    access['identity-endpoint'] = endpoint

    return res.status_code, access
