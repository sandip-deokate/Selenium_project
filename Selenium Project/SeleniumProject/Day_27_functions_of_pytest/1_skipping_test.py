import pytest

class TestClass():
    def test_LoginByYouTube(self):
        print("method1")

    def test_LoginByInsta(self):
        print("method2")

    def test_LoginByFacebook(self):
        print("method3")

    @pytest.mark.skip
    def Test_signUpByTouTube(self):
        print("method4")