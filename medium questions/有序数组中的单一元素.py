def singleNonDuplicate(nums: list) -> int:
    i = 1
    if len(nums) == 1:
        return nums[0]
    else:
        if (nums[0]-nums[1]) != 0:
            return nums[0]
        elif (nums[len(nums)-1]-nums[len(nums)-2]) != 0:
            return nums[len(nums)-1]
        else:
            while not((nums[i-1]-nums[i])and(nums[i]-nums[i+1])):
                i += 1
            return nums[i]


if __name__ == "__main__":
    N = [1, 1, 2, 3, 3, 4, 4, 8, 8]
    print(singleNonDuplicate(N))