import json
import xlwt


def read_text():
    with open("numbers.txt", encoding='UTF-8') as f:
        return f.read()


def write_excel(infos: dict):
    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet('numbers')

    for row_index,row in enumerate(infos):
        for column_index,column_value in enumerate(row):
            worksheet.write(row_index, column_index, label=column_value)

    workbook.save("numbers.xls")


if __name__ == "__main__":
    text = read_text()
    infos = json.loads(text)
    print(infos)
    write_excel(infos)
