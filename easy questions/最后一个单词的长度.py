def lengthOfLastWord(s: str) -> int:
    if not s:
        return 0
    if s[-1] == " ":
        while s[-1] == " ":
            s = s[:-1]
            if not s:
                return 0
    for i in range(len(s)):
        if s[-1-i] == " ":
            return i
    return len(s)


if __name__ == "__main__":
    a = "Hello World"
    b = "abc      "
    c = " "
    print(lengthOfLastWord(c))