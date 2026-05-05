import allure
import pytest

from testcases.common_tool.request_util import request_way


@allure.epic('医疗平台测试')
@allure.feature('医生模块')
@allure.story('医生接口关联测试')
class TestPatientFlow:
    @pytest.mark.smoke
    @pytest.mark.doctor
    def test_doctor_flow(self, base_url, auth_headers):
        allure.step('获取医生列表')
        doctor_list= request_way('get',f'{base_url}/api/doctors', headers=auth_headers)
        assert doctor_list.status_code == 200
        doctors = doctor_list.json()
        doctors = doctors['data']['list']
        assert len(doctors) > 0

        allure.step('提取第一个医生ID')
        first_doctor_id=doctors[0]['id']
        allure.attach(f'提取的第一个医生ID为{first_doctor_id}')

        allure.step(f'查询医生{first_doctor_id}的详情')
        detail_doctor_rep=request_way('get', f'{base_url}/api/doctors/{first_doctor_id}',headers=auth_headers)
        assert detail_doctor_rep.status_code == 200
        doctor_detail=detail_doctor_rep.json()['data']
        assert len(doctor_detail) > 0 ,'获取失败'

        allure.step('验证详情数据')
        assert first_doctor_id == doctor_detail['id']
        assert 'name' in doctor_detail
        assert 'department' in doctor_detail

        allure.attach(
            str(doctor_detail),
            name="医生详情",
            attachment_type=allure.attachment_type.JSON
        )








