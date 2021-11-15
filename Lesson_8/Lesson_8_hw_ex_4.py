class Storage:
    def __init__(self):
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
            self.storage_printer_count += 1
        elif isinstance(off_eq, Scanner):
            self.storage_scanners[off_eq.__str__()] = off_eq.__dict__
            self.storage_scanner_count += 1
        elif isinstance(off_eq, Xerox):
            self.storage_xerox[off_eq.__str__()] = off_eq.__dict__
            self.storage_xerox_count += 1
        else:
            print('Unknown object')


class OfficeEquipment:
    all_count = 0
    printer_count = 0
    scanner_count = 0
    xerox_count = 0

    def __init__(self, company, model, speed, colour):
        self.company = company
        self.model = model
        self.speed = speed
        self.colour = colour

    def __str__(self):
        return f'{self.company}:{self.model}'


class Printer(OfficeEquipment):
    def __init__(self, company, model, speed, colour):
        super().__init__(company, model, speed, colour)
        OfficeEquipment.printer_count += 1


class Scanner(OfficeEquipment):
    def __init__(self, company, model, speed, colour):
        super().__init__(company, model, speed, colour)
        OfficeEquipment.scanner_count += 1


class Xerox(OfficeEquipment):
    def __init__(self, company, model, speed, colour):
        super().__init__(company, model, speed, colour)
        OfficeEquipment.xerox_count += 1


xerox = Xerox('Samsung', 'HHJ101', 1, 1)
printer = Printer('Sony', 'MK45', 1, 1)
print(xerox.__dict__)
print(OfficeEquipment.xerox_count)

print('-------------------------------------')
storage = Storage()
print(storage.storage_printers)
storage.store_in(xerox)
storage.store_in(printer)
print(storage.storage_printers)
print(storage.storage_xerox)
print(isinstance(xerox, Xerox))
