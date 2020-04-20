from appium import webdriver
import pytest
import allure


class TestContact:
    # @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    @allure.step(title="登录的测试脚本")
    def test_login(self):
        allure.attach("输入用户名", "测试输入了，hello，1，str")
        print("输入用户名")
        self.xxx_page.input_login_edit_text()
        allure.attach("输入密码", "输入密码的描述")
        print("输入密码")
        allure.attach("登录", "登录的描述")
        print("点击登录")

        assert 1

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.step(title="用户名的测试脚本")
    def test_username(self):

        assert 1

    @pytest.allure.severity(pytest.allure.severity_level.TRIVIAL)
    @allure.step(title="密码的测试脚本")
    def test_passwo1d(self):

        assert 1