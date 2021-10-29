import sys

money, num1, num2, num3 = sys.argv


def babosu(a, b, c):
    return a * b + c


print(babosu(int(num1), int(num2), int(num3)))
