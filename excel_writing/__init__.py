import openpyxl
class ExcelTable:
    def __init__(self, path='/excel_database.xlsx'):
        self.path = path
    def write_data(self):
        with open(self.path, mode="w+"):
            pass

