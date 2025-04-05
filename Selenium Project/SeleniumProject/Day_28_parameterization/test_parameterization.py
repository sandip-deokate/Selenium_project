
import pytest

class TestClass():
    @pytest.mark.parametrize('num1,num2',[(1,1),(2,3),(5,5)])
    def test_test1(self,num1,num2):
        assert num1==num2