import pytest

class TestClass():
    @pytest.mark.fourth
    def test_test1(self):
        print("method1")

    @pytest.mark.third
    def test_test2(self):
        print("method2")

    @pytest.mark.second
    def test_test3(self):
        print("method3")

    @pytest.mark.first
    def test_test4(self): 
        print("method4")