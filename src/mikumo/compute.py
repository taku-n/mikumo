# Compute API v2

import requests

from . import util

def get_vms_list(access):
    """
    VM 一覧取得  
    https://www.conoha.jp/docs/compute-get_vms_list.php
    """
    token, endpoint = util.get_token_and_endpoint(access, 'compute')

    header = {'X-Auth-Token': token}
    res = requests.get(endpoint + '/servers', headers = header)
 
    return res.status_code, res.json()
