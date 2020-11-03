def isPalindrome(x: int) -> bool:
    lst = list(str(x))
    while len(lst) > 1:
        if lst.pop(0) != lst.pop():
            return False
    return True


if __name__ == "__main__":
    print(isPalindrome(2))