class Master:
    storages = {}

    @staticmethod
    def start_execution():
        department = Master.enter_department()
        if not Master.check('department', department):
            print('%' * 35 + '  !!!  PROGRAM ABORTED  !!!  ' + '%' * 35)
            return False
        choose = Master.enter_choose()
        if not Master.check('choose', choose):
            print('%' * 35 + '  !!!  PROGRAM ABORTED  !!!  ' + '%' * 35)
            return False
        list_data = Master.enter_list_data()
        if not Master.check('list_data', list_data):
            print('%' * 35 + '  !!!  PROGRAM ABORTED !!!  ' + '%' * 35)
            return False
        if department in Master.storages.keys():
            Master.__execution_part_2(department, choose, list_data)
        else:
            Master.storages[department] = Storage(department)
            Master.__execution_part_2(department, choose, list_data)

    @staticmethod
    def enter_department():
        department = input('Введите название подразделения : ')
        return department

    @staticmethod
    def enter_choose():
        choose = input('Введите: \n P для добавления принтера \n S для добавления сканнера \n '
                       'X для добавления ксерокса\n')
        return choose

    @staticmethod
    def enter_list_data():
        list_data = input('Введите через пробел название компании производителя, '
                          'модель, цвет и количество: ').split()
        return list_data

    @staticmethod
    def __execution_part_2(department, choose, list_data):
        if choose == 'P':
            Master.storages[department].store_in(Printer(list_data[0], list_data[1], list_data[2], list_data[3]))
        elif choose == 'S':
            Master.storages[department].store_in(Scanner(list_data[0], list_data[1], list_data[2], list_data[3]))
        elif choose == 'X':
            Master.storages[department].store_in(Xerox(list_data[0], list_data[1], list_data[2], list_data[3]))
        else:
            print('Facepalm')

    @staticmethod
    def check(what_to_check, check):
        result = True
        if what_to_check == 'department':
            pass
        #     здесь может быть проверка на существующие подразделения
        elif what_to_check == 'choose':
            if check != 'P' and check != 'S' and check != 'X':
                print('Unknown parameter')
                return False
        elif what_to_check == 'list_data':
            try:
                int(check[3])
            except ValueError:
                print('Wrong amount')
                result = False
            if len(check) > 4:
                print('There are extra parameters')
                result = False
        return result


class Storage:
    def __init__(self, department):
        self.department = department
        self.storage_printer_count = 0
        self.storage_scanner_count = 0
        self.storage_xerox_count = 0
        self.storage_all_count = 0
        self.storage_printers = {}
        self.storage_scanners = {}
        self.storage_xerox = {}

    def store_in(self, off_eq):
        if isinstance(off_eq, Printer):
            self.storage_printers[str(off_eq)] = off_eq.__dict__
        elif isinstance(off_eq, Scanner):
            self.storage_scanners[off_eq.__str__()] = off_eq.__dict__
        elif isinstance(off_eq, Xerox):
            self.storage_xerox[off_eq.__str__()] = off_eq.__dict__
        else:
            print('Unknown object')


class OfficeEquipment:

    def __init__(self, company, model, colour, count):
        self.company = company
        self.model = model
        self.colour = colour
        self.count = count

    def __str__(self):
        return f'{self.company}:{self.model}'


class Printer(OfficeEquipment):
    # просто так
    def __init__(self, company, model, colour, count):
        super().__init__(company, model, colour, count)


class Scanner(OfficeEquipment):
    # просто так
    def __init__(self, company, model, colour, count):
        super().__init__(company, model, colour, count)


class Xerox(OfficeEquipment):
    # просто так
    def __init__(self, company, model, colour, count):
        super().__init__(company, model, colour, count)


xerox = Xerox('Samsung', 'HHJ101', 1, 1)
printer = Printer('Sony', 'MK45', 1, 1)
# print(xerox.__dict__)
storage = Storage('Moscow Dep')
# print(storage.storage_printers)
# storage.store_in(xerox)
# storage.store_in(printer)
# print(storage.storage_printers)
# print(storage.storage_xerox)
# print(isinstance(xerox, Xerox))
# # OfficeEquipment.start_execution()
# print(storage.storage_printers)
# print('-' * 50)
# Master.storages['Wololo'] = Storage('Wololo')
# Master.storages['Wololo'].store_in(printer)
# print(Master.storages['Wololo'].storage_printers)
# Master.storages['Wololo'] = Storage('Wololo')
# print(Master.storages)
# print(Master.storages['Wololo'].storage_printers)
# print(Master.storages['Wololo'] in Master.storages)
# if 'Wololo' in Master.storages.keys():
#     print('wololo')
Master.start_execution()
# print(Master.storages['Muhaha'].storage_printers)
# print(Master.storages['Wololo'].storage_printers)
print('%' * 100)
# storage.store_in(xerox)
# print(str(xerox))
# print(xerox.__str__())
