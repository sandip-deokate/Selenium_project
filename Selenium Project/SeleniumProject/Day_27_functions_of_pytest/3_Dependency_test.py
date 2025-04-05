import pytest

class TestClass():

    @pytest.mark.dependency()
    def test_OpenBrowser(self):
        print("method1")
        assert False

    @pytest.mark.dependency(depends=['TestClass::test_OpenBrowser'])
    def test_Login(self):
        print("method2")
        assert True
    @pytest.mark.dependency(depends=["TestClass::test_OpenBrowser","TestClass::test_Login"])
    def test_Search(self):
        print("method3")
        assert True

    def test_AddToCart(self):
        print("method4")
        assert True

    @pytest.mark.dependency(depends=["TestClass::test_Login"])
    def test_Logout(self):
        print("method5")
        assert True