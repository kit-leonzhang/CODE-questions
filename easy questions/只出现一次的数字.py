def singleNumber(nums: list) -> int:
    a = []
    for i in range(len(nums)):
        if nums[i] in a:
            a.remove(nums[i])
            continue
        a.append(nums[i])
    return a[0]


if __name__ == "__main__":
    N = [1, 2, 4, 2, 1]
    print(singleNumber(N))