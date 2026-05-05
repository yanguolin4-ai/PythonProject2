import json
import pytest
import requests

from config_util import get_base_url


@pytest.fixture(scope='session')
def base_url():
    return get_base_url()

@pytest.fixture(scope='session')
def auth_token(base_url):
    rep=requests.post(f'{base_url}/api/auth/login', data={'username': 'admin', 'password': '123456'})
    assert rep.status_code == 200,f'获取token失败{rep.text}'
    token = json.loads(rep.text)
    token = token['data']['token']
    return token

@pytest.fixture(scope='session')
def auth_headers(auth_token):
    return {"Content-Type": "application/json",
             "Authorization": f"Bearer {auth_token}"
            }