import uuid

codes = []

for i in range(0, 100):
    codes.append(uuid.uuid1().hex.upper())

print(codes)
