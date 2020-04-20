import pytest


class TestLogin:
    @pytest.mark.parametrize("keys", ["1", "2"])
    def test_search(self, keys):
        print(keys)

    # @pytest.mark.parametrize(("username", "password"), [("zhangsan", "123"), ("lisi", "456")])
    # def test_search(self, username, password):
    #     print(username)
    #     print(password)
    #     print("-----")