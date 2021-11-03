import json

# from os import remove
#
# remove('ex_7_json.json')

with open('ex_7.txt', 'r') as f:
    list_demo = f.readlines()
list_profit = [int(el.split()[2]) for el in list_demo if int(el.split()[2]) - int(el.split()[3]) > 0]
list_master = [{el.split()[0]: (int(el.split()[2]) - int(el.split()[3])) for el in list_demo},
               {'average profit': sum(list_profit) / len(list_profit)}]
print(list_master)

with open('ex_7_json.json', 'x') as f:
    json.dump(list_master, f)
