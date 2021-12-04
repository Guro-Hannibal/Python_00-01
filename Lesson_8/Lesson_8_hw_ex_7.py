import math


class ComplexNumbers:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        print(f'z = {self.a} + {self.b}i')
        return ''

    def __add__(self, other):
        return ComplexNumbers(self.a + other.a, self.b + other.b)

    def __sub__(self, other):
        a = self.a - other.a
        b = self.b - other.b
        return ComplexNumbers(a, b)

    def __mul__(self, other):
        a = self.a * other.a + self.b * other.b * -1
        b = self.b * other.a + self.a * other.b
        return ComplexNumbers(a, b)

    def __truediv__(self, other):
        if other.b < 0:
            a1 = self.a * other.a + self.b * -other.b * -1
            a2 = self.b * other.a + self.a * -other.b
        else:
            a1 = self.a * other.a + self.b * other.b * -1
            a2 = self.b * other.a + self.a * other.b
        b = pow(other.a, 2) - pow(other.b, 2) * -1
        return ComplexNumbers(a1 / b, a2 / b)


c_num = ComplexNumbers(5, -24)
c_num_2 = ComplexNumbers(-45, -3)
c_num.__str__()
c_num_3 = c_num + c_num_2
str(c_num_3)
print(math.sqrt(3))
print(1.7320508075688772 * 1.7320508075688772)
print(math.sqrt(73))
print(math.sqrt(85))
print(3--2)
print(c_num - c_num_2)
print(c_num * c_num_2)
num = -5
c_num = ComplexNumbers(7, -6)
c_num_2 = ComplexNumbers(16, -8)
print(-num)
print(c_num / c_num_2)
print(-6 ** 2)
print(pow(-6, 2))
