import json
import xlwt


def read_text():
    with open("student.txt", encoding='UTF-8') as f:
        return f.read()


def write_excel(infos: dict):
    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet('student')

    row = 0
    for k in sorted(infos.keys()):
        worksheet.write(row, 0, label=k)
        for index, value in enumerate(infos[k]):
            worksheet.write(row, index + 1, label=value)

        row += 1

    workbook.save("student.xls")


if __name__ == "__main__":
    text = read_text()
    infos = json.loads(text)
    print(infos)
    write_excel(infos)
