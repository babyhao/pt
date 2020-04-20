import random

import pytest

class TestLogin:
    # 预期失败，结果成功：大写的黄色X
    @pytest.mark.xfail(True, reason="预期失败，结果成功")
    def test_login1(self):
        print("---test_login1，预期失败，结果成功 xfailed")
        assert True

    # 预期失败，结果失败：小写的黄色x
    @pytest.mark.xfail(True, reason="预期失败，结果失败")
    def test_login2(self):
        print("---test_login2，预期失败，结果失败 xpassed")
        assert False

    # 预期成功，结果成功：黄色的.
    @pytest.mark.xfail(False, reason="预期成功，结果成功")
    def test_login3(self):
        print("---test_login3，预期成功，结果成功 passed")
        assert True

    # 预期成功，结果失败：红色大写F
    @pytest.mark.xfail(False, reason="预期成功，结果失败")
    def test_login4(self):
        print("---test_login4，预期成功，结果失败 failed")
        assert False

    # @pytest.mark.skipif(True, reason="")
    # def test_login1(self):
    #     print("111")
    #     assert True
    #
    # def test_login2(self):
    #     print("2")
    #     assert True