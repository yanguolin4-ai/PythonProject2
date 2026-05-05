import pytest
import os
from allure_combine import combine_allure

if __name__ == '__main__':
    if os.path.exists("allure_report/temps"):
        os.system("rmdir /s /q allure_report\\temps")
    if os.path.exists("reports/allures"):
        os.system("rmdir /s /q reports\\allures")

    pytest.main([
        '-vs',
        '--alluredir=allure_report/temps'
    ])

    os.system("allure generate allure_report/temps -o reports/allures --lang zh --clean")

    combine_allure("./reports/allures", "./reports")