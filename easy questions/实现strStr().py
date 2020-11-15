def strStr(haystack: str, needle: str) -> int:
    if needle == []:
        return 0
    else:
        H = len(haystack)
        N = len(needle)
        for i in range(H-N+1):
            if needle == haystack[i:i+N]:
                return i
        return -1


if __name__ == "__main__":
    hay = "hello"
    ne = ""
    print(strStr(hay, ne))