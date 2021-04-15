from pprint import pprint

def print_access(access):
    pprint(access)

def print_endpoint(access):
    print(f'{"identity":>15}: {access["identity-endpoint"]}')
    for service in access['access']['serviceCatalog']:
        if service['type'] != 'identity':
            if 'publicURL' in service['endpoints'][0]:
                print(f'{service["type"]:>15}: {service["endpoints"][0]["publicURL"]}')

def get_token_and_endpoint(access, type):
    token = access['access']['token']['id']

    for service in access['access']['serviceCatalog']:
        if service['type'] == type:
            endpoint = service['endpoints'][0]['publicURL']

    return token, endpoint
