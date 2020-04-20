# pip install pytest-ordering
import pytest
import os


class TestABC:
    @pytest.mark.run(order=1)
    def test_a(self):
        print('1')
        assert True

    @pytest.mark.run(order=0)
    def test_b(self):
        print('0')
        print(os.getcwd())
        assert True

    @pytest.mark.run(order=4.3)
    def test_c(self):
        print('4.3')
        assert True

    @pytest.mark.run(order=-4)
    def test_d(self):
        print('-4')
        assert True

    @pytest.mark.run(order=-2)
    def test_e(self):
        print('-2')
        assert True

    def test_f(self):
        print('None')
        assert True


# 执行优先级
# 0 > 较小的正数 > 较大的正数 > 无标记 > 较小的负数 > 较大的负数