#------------------------读patients.yml文件-------------------------------------
import allure
import pytest
from testcases.common_tool.allure_util import allure_attach_response
from testcases.common_tool.read_yml_tool import read_yml
from testcases.common_tool.request_util import request_way


@allure.epic('医疗平台测试')
@allure.feature('患者模块读取')
@allure.story('患者接口')
@pytest.mark.smoke
@pytest.mark.patient
@pytest.mark.parametrize('caseinfo',read_yml('./testcases/usermanage/patients.yml'))
def test_read_patients(caseinfo,auth_headers):
    allure.dynamic.title(caseinfo['name'])
    allure.dynamic.description(caseinfo['description'])
    url=caseinfo['request']['url']
    rep= request_way(caseinfo['request']['method'], url=url ,headers=auth_headers)
    allure_attach_response(rep)


