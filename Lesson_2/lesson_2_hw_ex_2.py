try:
    list_len = int(input('Выберите длинну списка: '))
except ValueError:
    print('facepalm')

list_exm = []

while 0 != list_len:
    list_exm.append(input('Что угодно: '))
    list_len -= 1
print(list_exm)
y = None
i = 0
# print(len(list_exm))
while i < len(list_exm)-1:
    y = list_exm[i]
    # print(y)
    list_exm[i] = list_exm[i+1]
    # print(list_exm[i])
    list_exm[i+1] = y
    # print(list_exm[i])
    i += 2
    # print(list_exm)
print(list_exm)
