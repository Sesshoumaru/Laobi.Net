def read_excel():
    import xlrd
    with xlrd.open_workbook("numbers.xls") as f:
        sheet = f.sheet_by_index(0)
        row_count = sheet.nrows
        column_count = sheet.ncols
        result = []
        for row in range(row_count):
            values = []
            for column in range(0, column_count):
                values.append(sheet.cell(row, column).value)

            result.append(values)
        return result


def wirte_xml(infos):
    import xml.dom.minidom
    import json

    impl = xml.dom.minidom.getDOMImplementation()
    dom = impl.createDocument(None, 'root', None)
    root = dom.documentElement
    stduent = dom.createElement("numbers")
    comment = dom.createComment('数字信息')
    stduent.appendChild(comment)

    josn_text = json.dumps(infos,ensure_ascii=False)
    print(josn_text)
    text = dom.createCDATASection(josn_text)
    stduent.appendChild(text)
    root.appendChild(stduent)
    print(dom.toprettyxml() )

    f = open('numbers.xml', 'w', encoding='utf-8')
    dom.writexml(f, addindent='', newl='', encoding='utf-8')

if __name__ == "__main__":
    infos = read_excel()
    wirte_xml(infos)
