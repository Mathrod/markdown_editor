def object_with_beautiful_identity():
    for i in range(10_000):
        identity = id(i)
        if identity % 1000 == 888:
            return i


