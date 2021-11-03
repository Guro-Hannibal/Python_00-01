def to_digits(item):
    demo = ''
    for char in item:
        if char.isdigit():
            demo += char
    if demo == '':
        demo = 0
    return int(demo)


dict_demo = {}
with open('ex_6.txt', 'r', encoding='utf-8') as f:
    for line in f:
        name, lecture, practice, lab = line.split()
        dict_demo[name] = to_digits(lecture) + to_digits(practice) + to_digits(lab)

print(dict_demo)
