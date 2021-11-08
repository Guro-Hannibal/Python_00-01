# import os
#
# os.remove('ex_5.txt')

with open('ex_5.txt', 'x') as f:
    f.write(input('набор чисел разделенных пробелами --> '))
with open('ex_5.txt', 'r') as f:
    list_demo = [int(num) for num in f.read().split()]
print(sum(list_demo))
