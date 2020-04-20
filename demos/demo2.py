import allure


class TestABC:
    def setup(self):
        print('setUp')

    def teardown(self):
        print('teardown')

    @allure.severity('blocker')
    @allure.step(title='测试a')
    def test_a(self):
        allure.attach('测试a的描述','测试a的详细描述')
        print('test_a')
        assert True

    @allure.severity('critical')
    @allure.step(title='测试b')
    def test_b(self):
        allure.attach('测试b的描述','测试b的详细描述')
        allure.attach('测试b的描述2','测试b的详细描述2')
        print('test_b')
        assert True

    @allure.severity('normal')
    @allure.step(title='测试c')
    def test_c(self):
        print('test_c')
        assert True

    @allure.severity('minor')
    @allure.step(title='测试d')
    def test_d(self):
        print('test_d')
        assert True

    @allure.severity('trivial')
    @allure.step(title='测试e')
    def test_e(self):
        print('test_e')
        assert True
