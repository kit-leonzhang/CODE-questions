def removeDuplicates(nums: list) -> int:
        a = 0
        b = 1
        while b < len(nums):
            if nums[b] == nums[a]:
                b += 1
            else:
                a += 1
                nums[a] = nums[b]
        return a+1


if __name__ == "__main__":
    num = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(removeDuplicates(num))
    print(num)