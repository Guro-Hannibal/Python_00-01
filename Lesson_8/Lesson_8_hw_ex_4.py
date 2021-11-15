from abc import abstractmethod, ABC


class Master:
    storages = {}

    @staticmethod
    def start_execution():
        department = input('Введите название подразделения : ')
        choose = input('Введите: \n P для добавления принтера \n S для добавления сканнера \n '
                       'X для добавления ксерокса\n')
        list_data = input('Введите через пробел название компании производителя, '
                          'модель, цвет и количество: ').split()
        if department in Master.storages.keys():
            Master.__execution_part_2(department, choose, list_data)
        else:
            Master.storages[department] = Storage(department)
            Master.__execution_part_2(department, choose, list_data)

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
            self.storage_printers[off_eq.__str__()] = off_eq.__dict__
        elif isinstance(off_eq, Scanner):
            self.storage_scanners[off_eq.__str__()] = off_eq.__dict__
        elif isinstance(off_eq, Xerox):
            self.storage_xerox[off_eq.__str__()] = off_eq.__dict__
        else:
            print('Unknown object')


class OfficeEquipment(ABC):

    def __init__(self, company, model, speed, count):
        self.company = company
        self.model = model
        self.speed = speed
        self.count = count

    def __str__(self):
        return f'{self.company}:{self.model}'


class Printer(OfficeEquipment):
    # просто так
    def __init__(self, company, model, speed, count):
        super().__init__(company, model, speed, count)


class Scanner(OfficeEquipment):
    # просто так
    def __init__(self, company, model, speed, count):
        super().__init__(company, model, speed, count)


class Xerox(OfficeEquipment):
    # просто так
    def __init__(self, company, model, speed, count):
        super().__init__(company, model, speed, count)


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
# Master.start_execution()
# print(Master.storages['Muhaha'].storage_printers)
# print(Master.storages['Wololo'].storage_printers)
storage.store_in(xerox)
print(str(xerox))
print(xerox.__str__())
