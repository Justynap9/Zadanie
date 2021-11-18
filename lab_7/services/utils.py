def read_file(path: str):
    f = open(path, encoding = 'UTF8')
    data = f.read()
    f.close()
    return data