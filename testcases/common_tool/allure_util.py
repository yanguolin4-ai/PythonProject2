import allure
import json

from testcases.common_tool.request_util import request_way


def allure_attach_request_info(caseinfo,base_url):

    allure.attach(body=caseinfo['request']['url'], name="请求地址", attachment_type=allure.attachment_type.TEXT)
    allure.attach(body=json.dumps(caseinfo['request']['headers'], ensure_ascii=False, indent=2), name="请求头",
                  attachment_type=allure.attachment_type.TEXT)
    allure.attach(body=caseinfo['request']['method'], name="请求方法", attachment_type=allure.attachment_type.TEXT)
    allure.attach(body=json.dumps(caseinfo['request']['data'], ensure_ascii=False, indent=2),
                  name="请求数据",
                  attachment_type=allure.attachment_type.TEXT)
    rep = request_way(caseinfo['request']['method'], url=f'{base_url}/api/auth/login')
    if rep.status_code == 200:
        token = rep.json()['data']['token']
        allure.attach(body=token, name="取得的token", attachment_type=allure.attachment_type.TEXT)

def allure_attach_response(rep):
    allure.attach(body=rep.text, name="响应数据", attachment_type=allure.attachment_type.TEXT)
    allure.attach(body=str(rep.status_code),name='响应状态码',attachment_type=allure.attachment_type.TEXT)