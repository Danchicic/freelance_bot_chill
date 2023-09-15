from openpyxl.reader.excel import load_workbook

from telegram_requesting import get_request_from_bot


def usage_table(path: str = './exel_database.xlsx'):
    wb = load_workbook(path)
    sheet = wb['main']
    new_inn_index = 1
    # main iterator
    while sheet[f"A{new_inn_index}"].value is not None:
        inn_cell = sheet[f"A{new_inn_index}"].value
        """telegram requesting func"""
        get_request_from_bot(inn_cell)

        new_inn_index += 1


if __name__ == '__main__':
    usage_table()
