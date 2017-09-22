import uuid
import pymysql


def getcodes():
    codes = []
    for i in range(0, 100):
        codes.append(uuid.uuid1().hex.upper())

    return codes


def savecodes(codes):
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd='', database='test')
    cursor = conn.cursor()
    for i in range(0, len(codes)):
        cursor.execute("insert into code(id,code) VALUES (%s,%s)", (i, codes[i]))
    conn.commit()
    conn.close()


codes = getcodes()
print(codes)
savecodes(codes)
print('成功保存到mysql')
