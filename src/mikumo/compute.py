import requests

username = 'hoge'
password = 'fuga'
tenant_id = '0'
#token = '0'
token = '0'

header = {'X-Auth-Token': token, 'tenant_id': tenant_id}
res = requests.get('https://compute.tyo2.conoha.io/v2/0/servers',
        headers = header)
print(res.status_code)
print(res.json())
