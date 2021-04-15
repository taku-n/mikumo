# DNS API v1.0

import json
import requests

from . import util

def get_version(access):
    """
    バージョン情報取得  
    https://www.conoha.jp/docs/paas-dns-get-version-list.php
    """
    token, endpoint = util.get_token_and_endpoint(access, 'dns')

    res = requests.get(endpoint + '/')

    return res.status_code, res.json()

def get_server_hosting_domain(access, domain_id):
    """
    ドメインホスティング情報表示  
    https://www.conoha.jp/docs/paas-dns-get-servers-hosting-a-domain.php
    """
    token, endpoint = util.get_token_and_endpoint(access, 'dns')

    header = {'X-Auth-Token': token}
    res = requests.get(endpoint + '/v1/domains/' + domain_id + '/servers', headers = header)

    return res.status_code, res.json()

def list_domain(access):
    """
    ドメイン一覧表示  
    https://www.conoha.jp/docs/paas-dns-list-domains.php
    """
    token, endpoint = util.get_token_and_endpoint(access, 'dns')

    header = {'X-Auth-Token': token}
    res = requests.get(endpoint + '/v1/domains', headers = header)

    return res.status_code, res.json()

def create_domain(access, name):
    """
    ドメイン作成  
    https://www.conoha.jp/docs/paas-dns-create-domain.php
    """
    token, endpoint = util.get_token_and_endpoint(access, 'dns')
    domain_name = name + '.'

    header = {'Content-Type': 'application/json', 'X-Auth-Token': token}
    payload = {'name': domain_name, 'email': 'postmaster@example.org'}
    res = requests.post(endpoint + '/v1/domains', headers = header, data = json.dumps(payload))

    return res.status_code, res.json()

def delete_domain(access, domain_id):
    """
    ドメイン削除  
    https://www.conoha.jp/docs/paas-dns-delete-a-domain.php
    """
    token, endpoint = util.get_token_and_endpoint(access, 'dns')

    header = {'X-Auth-Token': token}
    res = requests.delete(endpoint + '/v1/domains/' + domain_id, headers = header)

    return res.status_code, {}

def get_domain_info(access, domain_id):
    """
    ドメイン情報表示  
    https://www.conoha.jp/docs/paas-dns-get-a-domain.php
    """
    token, endpoint = util.get_token_and_endpoint(access, 'dns')

    header = {'Content-Type': 'application/json', 'X-Auth-Token': token}
    res = requests.get(endpoint + '/v1/domains/' + domain_id, headers = header)

    return res.status_code, res.json()

def update_domain(access, domain_id,
        ttl = 3600, email = 'postmaster@example.org', description = None, gslb = 0):
    """
    ドメイン更新  
    https://www.conoha.jp/docs/paas-dns-update-a-domain.php
    """
    token, endpoint = util.get_token_and_endpoint(access, 'dns')

    header = {'Content-Type': 'application/json', 'X-Auth-Token': token}
    payload = {'ttl': ttl, 'email': email, 'description': description, 'gslb': gslb}
    res = requests.put(endpoint + '/v1/domains/' + domain_id,
            headers = header, data = json.dumps(payload))

    return res.status_code, res.json()

def list_record(access, domain_id):
    """
    レコード一覧取得  
    https://www.conoha.jp/docs/paas-dns-list-records-in-a-domain.php
    """
    token, endpoint = util.get_token_and_endpoint(access, 'dns')

    header = {'Content-Type': 'application/json', 'X-Auth-Token': token}
    res = requests.get(endpoint + '/v1/domains/' + domain_id + '/records', headers = header)

    return res.status_code, res.json()

def create_record(access, domain_id, name, type, data, priority):
    """
    レコード作成  
    https://www.conoha.jp/docs/paas-dns-create-record.php  
    create_record(access, '12345678-1234-1234-1234-123456789abc', 'www', 'A', '192.168.1.1', None)
    """
    token, endpoint = util.get_token_and_endpoint(access, 'dns')
    code, domain_info = get_domain_info(access, domain_id)
    domain_name = domain_info['name']
    if name == '':
        fqdn = domain_name
    elif name == '@':
        fqdn = domain_name
    else:
        fqdn = name + '.' + domain_name

    header = {'Content-Type': 'application/json', 'X-Auth-Token': token}
    payload = {'name': fqdn, 'type': type, 'data': data, 'priority': priority}
    res = requests.post(endpoint + '/v1/domains/' + domain_id + '/records',
            headers = header, data = json.dumps(payload))

    return res.status_code, res.json()

def delete_record(access, domain_id, record_id):
    """
    レコード削除  
    https://www.conoha.jp/docs/paas-dns-delete-a-record.php
    """
    token, endpoint = util.get_token_and_endpoint(access, 'dns')

    header = {'Content-Type': 'application/json', 'X-Auth-Token': token}
    res = requests.delete(endpoint + '/v1/domains/' + domain_id + '/records/' + record_id,
            headers = header)

    return res.status_code, {}

def get_record_info(access, domain_id, record_id):
    """
    レコード情報表示  
    https://www.conoha.jp/docs/paas-dns-get-a-record.php
    """
    token, endpoint = util.get_token_and_endpoint(access, 'dns')

    header = {'Content-Type': 'application/json', 'X-Auth-Token': token}
    res = requests.get(endpoint + '/v1/domains/' + domain_id + '/records/' + record_id,
            headers = header)

    return res.status_code, res.json()

def update_record(access, domain_id, record_id, name, type, data, priority,
        ttl = None, description = None, gslb_region = None, gslb_weight = None, gslb_check = None):
    """
    レコード更新  
    https://www.conoha.jp/docs/paas-dns-update-a-record.php
    update_record(access,
            '12345678-1234-1234-1234-123456789abc', '89abcdef-cdef-cdef-cdef-456789abcdef'
            'www', 'A', '192.168.1.1', None)
    """
    token, endpoint = util.get_token_and_endpoint(access, 'dns')
    code, domain_info = get_domain_info(access, domain_id)
    domain_name = domain_info['name']
    if name == '':
        fqdn = domain_name
    elif name == '@':
        fqdn = domain_name
    else:
        fqdn = name + '.' + domain_name

    header = {'Content-Type': 'application/json', 'X-Auth-Token': token}
    payload = {'name': fqdn, 'type': type, 'data': data, 'priority': priority}
    res = requests.put(endpoint + '/v1/domains/' + domain_id + '/records/' + record_id,
            headers = header, data = json.dumps(payload))

    return res.status_code, res.json()

def import_zone(access, data):
    """
    ゾーンファイルインポート  
    https://www.conoha.jp/docs/paas-dns-import-zone.php
    """
    token, endpoint = util.get_token_and_endpoint(access, 'dns')

    header = {'Content-Type': 'text/dns', 'X-Auth-Token': token}
    res = requests.post(endpoint + '/v2/zones', headers = header, data = data)

    return res.status_code, res.json()

def export_zone(access, domain_id):
    """
    ゾーンファイルエクスポート  
    https://www.conoha.jp/docs/paas-dns-export-zone.php
    """
    token, endpoint = util.get_token_and_endpoint(access, 'dns')

    header = {'Accept': 'text/dns', 'X-Auth-Token': token}
    res = requests.get(endpoint + '/v2/zones/' + domain_id, headers = header)

    return res.status_code, res.text
