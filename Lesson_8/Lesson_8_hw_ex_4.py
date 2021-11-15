class Storage:
    storage_printer_count = 0
    storage_scanner_count = 0
    storage_xerox_count = 0
    storage_all_count = 0
    storage_printers = []
    storage_scanners = []
    storage_xerox = []

    def store_in(self, off_eq):
        self.storage_printers.append({off_eq.model: off_eq.__dict__})


class OfficeEquipment:
    all_count = 0
    printer_count = 0
    scanner_count = 0
    xerox_count = 0


class Printer(OfficeEquipment):
    def __init__(self, company, model, speed, colour):
        self.company = company
        self.model = model
        self.speed = speed
        self.colour = colour
        OfficeEquipment.printer_count += 1


class Scanner(OfficeEquipment):
    def __init__(self, company, model, speed, colour):
        self.company = company
        self.model = model
        self.speed = speed
        self.colour = colour
        OfficeEquipment.scanner_count += 1


class Xerox(OfficeEquipment):
    def __init__(self, company, model, speed, colour):
        self.company = company
        self.model = model
        self.speed = speed
        self.colour = colour
        OfficeEquipment.xerox_count += 1


xerox = Xerox(1, 1, 1, 1)
xerox2 = Xerox(1, 1, 1, 1)
print(xerox.__dict__)

print('-------------------------------------')
storage = Storage()
print(storage.storage_printers)
storage.store_in(xerox)
storage.store_in(xerox)
print(storage.storage_printers)
