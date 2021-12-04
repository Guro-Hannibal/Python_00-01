import math

# можно было бы унаследовать Exception, но тут это не нужно


class DivZero:

    def __init__(self, dividend, divisor):
        self.dividend = dividend
        self.divisor = divisor

    def divide(self):
        try:
            return self.dividend / self.divisor
        except ZeroDivisionError:
            return f'от {-math.inf} до {math.inf}'

    @staticmethod
    def dev_0(dividend, divisor):
        try:
            return dividend / divisor
        except ZeroDivisionError:
            return f'от {-math.inf} до {math.inf}'


print(DivZero.dev_0(10, 0))
demo = DivZero(50, 0)
print(demo.divide())
