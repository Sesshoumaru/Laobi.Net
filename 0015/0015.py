import json
import xlwt


def read_text():
    with open("city.txt", encoding='UTF-8') as f:
        return f.read()


def write_excel(infos: dict):
    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet('city')

    row = 0
    for k in sorted(infos.keys()):
        worksheet.write(row, 0, label=k)
        worksheet.write(row, 1, label=infos[k])

        row += 1

    workbook.save("city.xls")


if __name__ == "__main__":
    text = read_text()
    infos = json.loads(text)
    print(infos)
    write_excel(infos)
