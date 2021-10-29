seasons = ['winter is coming', 'spring is coming', 'summer is coming', 'autumn is coming']
key = int(input('номер месяца - '))
if key == 1 or key == 2 or key == 12:
    print(seasons[0])
elif key == 4 or key == 5 or key == 6:
    print(seasons[1])
elif key == 7 or key == 7 or key == 8:
    print(seasons[2])
elif key == 9 or key == 10 or key == 11:
    print(seasons[3])


# seasons_dict = {1: 'winter is coming', 2: 'winter is coming', 3: 'spring is coming',
#                 4: 'spring is coming', 5: 'spring is coming', 6: 'summer is coming',
#                 7: 'summer is coming', 8: 'summer is coming', 9: 'autumn is coming',
#                 10: 'autumn is coming', 11: 'autumn is coming', 12: 'winter is coming'}
# print(seasons_dict[key])
