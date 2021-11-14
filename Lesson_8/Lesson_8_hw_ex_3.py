demo_true = [12.69, '23', '43.420', 12, 65]
demo_false = [14, 54, '15', 'abc', 432, 43]


class CheckList:

    # проверка при инициализации в реальном времени

    def __init__(self):
        self.check_list = []
        while True:
            app_item = input('Wololo? To quit type Q -> ')
            if app_item == 'Q':
                break
            elif CheckList.is_num(app_item):
                self.check_list.append(float(app_item))
            else:
                print('Вы ввели не число')

    # проверка готового списка

    @staticmethod
    def is_num_list(demo_list):
        try:
            return all(isinstance(float(i), float) for i in demo_list)
        except ValueError:
            return False

    @staticmethod
    def is_num(check_num):
        try:
            isinstance(float(check_num), float)
            return True
        except ValueError:
            return False


print(CheckList.is_num_list(demo_true))
print(CheckList.is_num_list(demo_false))
demo = CheckList()
print(demo.check_list)
