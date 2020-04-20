# pip install pytest-rerunfailures
# import pytest
import os

def test_a():
    print('------>test_a')
    print(os.getcwd())
    assert 1

def test_b():
    print('------>test_b')
    assert 0



# if __name__ == '__main__':
#     pytest.main(['-s', 'demo1.py'])