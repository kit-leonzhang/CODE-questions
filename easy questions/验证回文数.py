def isPalindrome(s: str) -> bool:
    start = 0
    end = len(s) - 1
    if not s:
        return True
    if len(s) == 1:
        return True
    for i in range(len(s) - 1):
        if s[start].isalnum() and s[end].isalnum():
            if s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1
            continue
        if not s[start].isalnum() and s[end].isalnum():
            start += 1
            continue
        if s[start].isalnum() and not s[end].isalnum():
            end -= 1
            continue
        if not s[start].isalnum() and not s[end].isalnum():
            start += 1
            end -= 1
            continue
    return True


if __name__ == "__main__":
    N = "A man, a plan, a canal: Panama"
    print(isPalindrome(N))