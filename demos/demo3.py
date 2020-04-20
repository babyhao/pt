class TestABC:
    def setup_class(self):
        print('setup_class')

    def teardown_class(self):
        print('teardown_class')

    def setup(self):
        print('setUp')

    def teardown(self):
        print('teardown')

    def test_a(self):
        print('test_a')
        assert True

    def test_b(self):
        print('test_b')
        assert True

    def test_c(self):
        print('test_c')
        assert True