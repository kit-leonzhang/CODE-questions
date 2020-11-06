#def maxSubArray(nums: list) -> int:
#    lens = len(nums)
#    start = 0
#    end = 0
#    max = nums[0]
#    for i in range(lens):
#        sum = 0
#        for j in range(i, lens):
#            sum += nums[j]
#            if sum > max:
#                max = sum
#                start = i
#                end =j
#    print(nums[start:end+1])
#    return max


def maxSubArray(nums: list) -> int:
    lens = len(nums)
    sum = nums[0]
    maxs = sum
    for i in range(1, lens):
        sum += nums[i]
        if sum < nums[i]:
            start = i
            sum = nums[start]
            maxs = max(maxs, nums[start])
        else:
            maxs = max(maxs, sum)
    return maxs


if __name__ == "__main__":
    #N = [1, -2, 3, 4]
    N = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(maxSubArray(N))