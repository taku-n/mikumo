# Module mikumo.dns


## Functions

### create_domain 

```python
def create_domain(access, name)
```

ドメイン作成  
https://www.conoha.jp/docs/paas-dns-create-domain.php

------

### create_record 

```python
def create_record(access, domain_id, name, type, data, priority)
```

レコード作成  
https://www.conoha.jp/docs/paas-dns-create-record.php  
create_record(access, '12345678-1234-1234-1234-123456789abc', 'www', 'A', '192.168.1.1', None)

------

### create_record_by_domain_name 

```python
def create_record_by_domain_name(access, domain_name, name, type, data, priority)
```


------

### delete_domain 

```python
def delete_domain(access, domain_id)
```

ドメイン削除  
https://www.conoha.jp/docs/paas-dns-delete-a-domain.php

------

### delete_record 

```python
def delete_record(access, domain_id, record_id)
```

レコード削除  
https://www.conoha.jp/docs/paas-dns-delete-a-record.php

------

### delete_record_by_domain_name 

```python
def delete_record_by_domain_name(access, domain_name, record_id)
```


------

### delete_record_by_domain_name_and_name 

```python
def delete_record_by_domain_name_and_name(access, domain_name, name, type)
```


------

### export_zone 

```python
def export_zone(access, domain_id)
```

ゾーンファイルエクスポート  
https://www.conoha.jp/docs/paas-dns-export-zone.php

------

### get_domain_id 

```python
def get_domain_id(access, domain_name)
```


------

### get_domain_info 

```python
def get_domain_info(access, domain_id)
```

ドメイン情報表示  
https://www.conoha.jp/docs/paas-dns-get-a-domain.php

------

### get_record_id 

```python
def get_record_id(access, domain_id, name, type)
```


------

### get_record_id_by_domain_name 

```python
def get_record_id_by_domain_name(access, domain_name, name, type)
```


------

### get_record_info 

```python
def get_record_info(access, domain_id, record_id)
```

レコード情報表示  
https://www.conoha.jp/docs/paas-dns-get-a-record.php

------

### get_server_hosting_domain 

```python
def get_server_hosting_domain(access, domain_id)
```

ドメインホスティング情報表示  
https://www.conoha.jp/docs/paas-dns-get-servers-hosting-a-domain.php

------

### get_version 

```python
def get_version(access)
```

バージョン情報取得  
https://www.conoha.jp/docs/paas-dns-get-version-list.php

------

### import_zone 

```python
def import_zone(access, data)
```

ゾーンファイルインポート  
https://www.conoha.jp/docs/paas-dns-import-zone.php

------

### list_domain 

```python
def list_domain(access)
```

ドメイン一覧表示  
https://www.conoha.jp/docs/paas-dns-list-domains.php

------

### list_record 

```python
def list_record(access, domain_id)
```

レコード一覧取得  
https://www.conoha.jp/docs/paas-dns-list-records-in-a-domain.php

------

### list_record_by_domain_name 

```python
def list_record_by_domain_name(access, domain_name)
```


------

### update_domain 

```python
def update_domain(access, domain_id,
    ttl = 3600, email = 'postmaster@example.org', description = None, gslb = 0)
```

ドメイン更新  
https://www.conoha.jp/docs/paas-dns-update-a-domain.php

------

### update_record 

```python
def update_record(access, domain_id, record_id, name, type, data, priority,
    ttl = None, description = None, gslb_region = None, gslb_weight = None, gslb_check = None)
```

レコード更新  
https://www.conoha.jp/docs/paas-dns-update-a-record.php
update_record(access,
        '12345678-1234-1234-1234-123456789abc', '89abcdef-cdef-cdef-cdef-456789abcdef'
        'www', 'A', '192.168.1.1', None)
