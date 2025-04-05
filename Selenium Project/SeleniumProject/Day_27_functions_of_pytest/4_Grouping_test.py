import pytest

class TestClass():
    @pytest.mark.sanity
    def test_test1(self):
        print("method1")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_test2(self):
        print("method2")

    def test_test3(self):
        print("method3")

    @pytest.mark.regression
    def test_test4(self):
        print("method4")