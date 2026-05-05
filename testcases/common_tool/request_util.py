import requests

from conftest import auth_headers


def request_way(method, url, data=None, headers=None):
    if headers is None:
        headers = {"Content-Type": "application/json"}
    method = method.lower()
    if method == "get":
        return requests.get(url, params=data, headers=headers)
    elif method == "post":
        return requests.post(url, json=data, headers=headers)
    elif method == "put":
        return requests.put(url, json=data, headers=headers)
    elif method == "delete":
        return requests.delete(url, params=data, headers=headers)
    else:
        raise ValueError(f"不支持的请求方法: {method}")