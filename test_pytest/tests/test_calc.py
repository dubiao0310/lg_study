import allure
import pytest

from test_pytest.core.calc import Calc


class TestCalc:
    def setup_class(self):
        self.calc = Calc()

    def setup(self):
        pass

    @allure.story("乘法整数测试用例")
    @pytest.mark.parametrize('a, b, c', [
        [1, 2, 2],
        [-1, -1, 1],
        [1, -1, -1],
        [0, 1, 0],
        [1, 0, 0]
    ])
    def test_mul1(self, a, b, c):
        assert self.calc.mul(a, b) == c

    @allure.story("乘法浮点数测试用例")
    @pytest.mark.parametrize('a, b, c', [
        [0.5, 0.5, 0.25],
        [0, 0.5, 0],
        [0.5, 0, 0],
        [0.1, 0.1, 0.01],
    ])
    def test_mul2(self, a, b, c):
        assert self.calc.mul(a, b) == c

    @allure.story("乘法异常值测试用例")
    @pytest.mark.parametrize('a, b', [
        ["1", 0],
        [0, "1"],
        ["1", "1"]
    ])
    def test_mul3(self, a, b):
        with pytest.raises(Exception):
            assert self.calc.mul(a, b)

    @allure.story("正常值测试用例")
    @pytest.mark.parametrize('a, b, c', [
        [2, 2, 1],
        [0.2, 0.1, 2],
        [0, 2, 0]
    ])
    def test_div1(self, a, b, c):
        assert self.calc.div(a, b) == c

    @allure.story("异常值测试用例")
    @pytest.mark.parametrize('a, b', [
        [2, 0],
        [0.2, 0],
        [0, 0],
        ["1", 1],
        [1, "1"]
    ])
    def test_div2(self, a, b):
        with pytest.raises(Exception):
            assert self.calc.div(a, b)

    @allure.story("流程测试用例")
    def test_process(self):
        r1=self.calc.mul(1, 2)
        r2=self.calc.div(2, 1)
        assert r1 == 2
        assert r2 == 2



