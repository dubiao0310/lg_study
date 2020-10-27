import pytest

from test_pytest.core.calc import Calc


class TestCalc:
    def setup_class(self):
        self.calc = Calc()

    def setup(self):
        pass

    @pytest.mark.parametrize('a, b, c', [
        [1, 2, 2],
        [-1, -1, 1],
        [1, -1, 1]
    ])
    def test_mul(self, a, b, c):
        assert self.calc.mul(a, b) == c
        # assert calc.mul(-1, -1) == 1
        # assert calc.mul(1, -1) == 1

    @pytest.mark.parametrize('a, b, c', [
        [1, 2, 0.5],
        [-1, 2, -0.5],
        [1, -2, -0.5],
        [-1, -1, 1],
        [0, 1, 0],
        [1, 0, ]
    ])
    def test_div(self, a, b, c):
        assert self.calc.div(a, b) == c


