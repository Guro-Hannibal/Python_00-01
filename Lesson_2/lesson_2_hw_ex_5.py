my_list = [7, 5, 3, 3, 2]
my_list_copy = my_list

i = int(input('Число - '))
count = 0

if i > max(my_list_copy):
    my_list.insert(0, i)
# elif i == max(my_list_copy):
#     for item in my_list_copy:
#         if i == item:
#             count = my_list_copy.index(item)
#     my_list.insert(count, i)
#     print(count)
elif my_list_copy.__contains__(i):
    y = 0
    for item in my_list_copy:
        if i == item:
            y += 1
            count = my_list_copy.index(item) + y
    my_list.insert(count, i)
    print(count)
elif not my_list_copy.__contains__(i):
    my_list.append(i)
print(my_list)


# if my_list_copy.__contains__(i):
#     print('wuhuhu')