import json


def assert_status_code(rep, expectedcode):
    expected_code=expectedcode
    actualcode = rep.status_code
    assert actualcode == expected_code,f'状态码断言失败：期望 {expected_code}，实际 {actualcode}，响应内容：{rep.text}'

def assert_status_value(rep,key,expected_value):
    data=json.loads(rep.text)
    actual_value=data.get(key)
    assert actual_value==expected_value, f'应输出{expected_value},错误输出{actual_value}'