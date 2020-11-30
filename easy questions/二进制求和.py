def addBinary(a: str, b: str) -> str:
    if len(a) >= len(b):
        temp = b
        b = a
        a = temp
    add = 0
    c = []
    val = 0
    for i in range(len(b)):
        if i <= len(a) - 1:
            if int(a[-i-1]) + int(b[-i-1]) + add == 0:
                add = 0
                val = 0
            elif int(a[-i-1]) + int(b[-i-1]) + add == 1:
                add = 0
                val = 1
            elif int(a[-i-1]) + int(b[-i-1]) + add == 2:
                add = 1
                val = 0
            elif int(a[-i-1]) + int(b[-i-1]) + add == 3:
                add = 1
                val = 1
            c.insert(0, str(val))
        else:
            if int(b[-i-1]) + add == 0:
                val = 0
                add = 0
            elif int(b[-i-1]) + add == 1:
                val = 1
                add = 0
            elif int(b[-i-1]) + add == 2:
                val = 0
                add = 1
            c.insert(0, str(val))
    if add == 1:
        c.insert(0, '1')
    return "".join(c)


if __name__ == "__main__":
    A = "1010"
    B = "1011"
    print(addBinary(A, B))
