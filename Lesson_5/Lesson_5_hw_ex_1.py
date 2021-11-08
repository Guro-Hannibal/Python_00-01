# import os
#
# os.remove('ex_1.txt')

with open('ex_1.txt', 'x') as f:
    while True:
        a = input()
        if a == '':
            break
        f.write(a + '\n')
