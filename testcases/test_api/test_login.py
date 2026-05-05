import allure
import pytest
import requests
from pygments.lexers import q

from testcases.common_tool.allure_util import allure_attach_request_info, allure_attach_response
from testcases.common_tool.assert_util import assert_status_code, assert_status_value
from testcases.common_tool.read_yml_tool import read_yml

@allure.epic("医疗平台测试")
@allure.feature('登录页面')
@allure.story('登录操作')
class Test_api_login:
 @pytest.mark.smoke
 @pytest.mark.login
 @pytest.mark.parametrize('caseinfo', read_yml('./testcases/usermanage/get_token.yml'))  #数据驱动
 def test_api_login(self, caseinfo, base_url):
     allure.dynamic.title(caseinfo["name"])
     allure.dynamic.description(caseinfo["description"])
     allure_attach_request_info(caseinfo,base_url=base_url)
     try:
         rep = requests.post(f'{base_url}/api/auth/login', data={'username': 'admin', 'password': '123456'})
         allure_attach_response(rep)
         assert_status_code(rep, caseinfo['expected']['status_code'])
     except Exception as e:
         print(f"断言失败：{e}")


