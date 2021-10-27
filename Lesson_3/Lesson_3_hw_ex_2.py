# user = {'name': '', 'surname': '', 'date_of_birth': '', 'city': '', 'email': '', 'mobile_num': ''}


# def user_data_form():
#     for key in user.keys():
#         user[key] = input(f'Введите {key} : ')
#     return user


# print(user_data_form())


def another_user_data_form(name, surname, date, city, email, mobile_num):
    user = {'name': name, 'surname': surname, 'date_of_birth': date, 'city': city, 'email': email,
            'mobile_num': mobile_num}
    return user


print(another_user_data_form('name', 'surname', 'date', 'city', 'email', 'mobile'))
