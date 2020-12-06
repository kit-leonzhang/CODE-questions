def getRow(rowIndex: int) -> list:
    if rowIndex == 0:
        return [1]
    a = [1, 1]
    if rowIndex == 1:
        return a
    for i in range(2, rowIndex + 1):
        c = [1]
        for k in range(1, len(a)):
            c.append(a[k - 1] + a[k])
        c.append(1)
        a = c
    return a


if __name__ == "__main__":
    print(getRow(5))
