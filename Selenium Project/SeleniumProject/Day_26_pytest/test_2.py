import pytest


class TestA:
    @pytest.fixture()
    def setup(self):
        print("Lauch browser")
        print("open chrome")
        yield
        print("close broeser")


    def test_method1(self,setup):
        print("I am method1")
    def test_method2(self,setup):
        print("method2")

    def test_method3(self,setup):
        print("method3")