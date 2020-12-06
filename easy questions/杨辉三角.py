def generate(numRows: int) -> list:
    if numRows == 0:
        return []
    if numRows == 1:
        return [[1]]
    a = [1, 1]
    b = [[1], [1, 1]]
    if numRows == 2:
        return b
    for i in range(2, numRows):
        c = []
        c.append(1)
        for k in range(1, len(a)):
            c.append(a[k-1] + a[k])
        c.append(1)
        a = c
        b.append(a)
    return b


if __name__ == "__main__":
    print(generate(0))