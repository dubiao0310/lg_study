import math


class Calc:

    def div(self, a, b):
        return a/b

    def mul(self, a, b):
        return a*b


if __name__ == '__main__':
    calc = Calc()
    print(calc.div(1, 0))
    math