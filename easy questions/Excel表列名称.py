def convertToTitle(n: int) -> str:
    a = ''
    k = 1
    while n > 0:
        if n % (26 ** k) == 0:
            a += 'Z'
            n -= 26 ** k
            k += 1
            continue
        a += chr((n % (26 ** k)) // (26 ** (k - 1)) + 64)
        n -= (26 ** (k - 1)) * (n % (26 ** k) // (26 ** (k - 1)))
        k += 1
    return a[::-1]


if __name__ == "__main__":
    print(convertToTitle(703))