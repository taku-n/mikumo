import requests

from . import id

def get_token_and_endpoint(access):
    token = access['access']['token']['id']

    for service in access['access']['serviceCatalog']:
        if service['type'] == 'dns':
            endpoint = service['endpoints'][0]['publicURL']

    return token, endpoint

def ver(auth):
    endpoint = auth['dns']['endpoint']

    res = requests.get(endpoint + '/')

    id.hi()
    return res.status_code, res.json()

def list_domain(access):
    token = access['access']['token']['id']
    for service in access['access']['serviceCatalog']:
        if service['type'] == 'dns':
            endpoint = service['endpoints'][0]['publicURL']

    #code, token = id.get_token(auth)
    print(token)

    header = {'X-Auth-Token': token}
    res = requests.get(endpoint + '/v1/domains', headers = header)
    print(res.status_code)
    print(res.json())

def list_record(access, domain_id):
    token, endpoint = get_token_and_endpoint(access)

    header = {'X-Auth-Token': token}
    res = requests.get(endpoint + '/v1/domains/' + domain_id + '/records', headers = header)

    print(res.status_code)
    print(res.json())
