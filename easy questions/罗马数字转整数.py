#   秀操作就没意思了
#def romanToInt(s: str) -> int:
#    d = {'I': 1, 'IV': 3, 'V': 5, 'IX': 8, 'X': 10, 'XL': 30, 'L': 50, 'XC': 80, 'C': 100, 'CD': 300, 'D': 500,
#         'CM': 800, 'M': 1000}
#    return sum(d.get(s[max(i - 1, 0):i + 1], d[n]) for i, n in enumerate(s))


def romanToInt(s: str) -> int:
    Roman2Int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    Int = 0
    n = len(s)

    for index in range(n - 1):
        if Roman2Int[s[index]] < Roman2Int[s[index + 1]]:
            Int -= Roman2Int[s[index]]
        else:
            Int += Roman2Int[s[index]]

    return Int + Roman2Int[s[-1]]


if __name__ == "__main__":
    print(romanToInt("IV"))