def longestCommonPrefix(strs):
    if len(strs) == 0:
        return ''
    for i in range(len(strs[0])):
        c = strs[0][i]
        for j in range(1, len(strs)):
            if i == len(strs[j]) or strs[j][i] != c:
                return strs[0][0:i]
    return strs[0]


if __name__ == "__main__":
    N = ["flower", "flow", "flight"]
    print(longestCommonPrefix(N))