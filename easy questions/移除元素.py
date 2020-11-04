def removeElement(num: list,val: int) -> int:
    a = 0
    b = 0
    while a < len(num):
        if num[a] != val:
            num[b] = num[a]
            b += 1
        a += 1
    return b


if __name__ == "__main__":
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    c = 1
    print(removeElement(nums,c))
    print(nums)