class Data:
    def __init__(self, data_str):
        self.data_str = str(data_str)

    @classmethod
    def data_to_int_list(cls, data_str):
        return [int(i) for i in data_str.split('-')]

    @staticmethod
    def validation(data_str):
        data_int = Data.data_to_int_list(data_str)
        success = 1
        if 1 > data_int[0] or data_int[0] > 31:
            print('Incorrect day')
            success = 0
        if 1 > data_int[1] or data_int[1] > 12:
            print('Incorrect month')
            success = 0
        if data_int[2] > 2021:
            print('Incorrect year')
            success = 0
        if success:
            print('Validation successful')
        return bool(success)


revolution = Data('31-11-2013')
print(revolution.validation('31-11-2013'))
print(Data.data_to_int_list('331 - 11 - 2013'))
# Data.validation('331 - 11 - 2013')
print(Data.validation('331 - 11 - 2013'))
