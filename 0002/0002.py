def getcodes():
    import uuid
    codes = []
    for i in range(0, 100):
        codes.append(uuid.uuid1().hex.upper())

    return codes


codes = getcodes()
print(codes)
