#------------------------拔取页面患者数据并且与yml文件作比较------------------------------
import allure
import json
import pytest
import requests


@allure.epic('医疗平台测试')
@allure.feature('患者模块')
@allure.story('患者接口关联测试')
class TestPatientFlow:

    @pytest.mark.smoke
    @pytest.mark.patient
    def test_patient_flow(self, base_url, auth_headers):
        allure.step('获取患者列表')
        list_patient=requests.get(url=f'{base_url}/api/patients',headers=auth_headers,params={"page":1,"per_page":10})
        assert list_patient.status_code == 200,'获取失败'
        list_patient_flow=json.loads(list_patient.text)
        patient=list_patient_flow['data']['list']
        assert len(patient) > 0,'患者列表为空'

        allure.step('提取第一个缓则 ID')
        first_patient_id=patient[0]['id']
        allure.attach(f'提取到的患者ID：{first_patient_id}',name='patient_id')

        allure.step(f'查询患者{first_patient_id}的详情')
        detail_resp=requests.get(
            f'{base_url}/api/patients/{first_patient_id}',
            headers=auth_headers,
        )
        assert detail_resp.status_code == 200
        patient_detail=detail_resp.json()['data']

        allure.step('验证详情数据')
        assert patient_detail['id'] == first_patient_id
        assert 'name' in patient_detail
        assert 'department' in patient_detail

        allure.attach(
            str(patient_detail),
            name="患者详情",
            attachment_type=allure.attachment_type.JSON
        )




