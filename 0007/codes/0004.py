import uuid
from pyredis import Client


def getcodes():
    codes = []
    for i in range(0, 100):
        codes.append(uuid.uuid1().hex.upper())

    return codes


def savecodes(codes):
    client = Client(host="localhost")
    for code in codes:
        client.lpush('codes', code)
    client.close()


def checkcodessaved():
    client = Client(host="localhost")
    print(client.lrange('codes', 0, 100))
    client.close()


codes = getcodes()
# print(codes)
savecodes(codes)
checkcodessaved()
print('成功保存到redis')
