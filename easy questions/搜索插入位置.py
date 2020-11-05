# 暴力搜索法
# def searchInsert(nums: list , target: int) -> int:
#   if nums[-1] < target:
#         return len(nums)
#    else:
#        for i in range(len(nums)):
#            if nums[i] >= target:
#                return i
#                break


def searchInsert(nums: list, target: int) -> int:
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2   #  // 代表整除向下取整
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left


if __name__ == "__main__":
    N = [1, 3, 5, 6]
    T = 7
    print(searchInsert(N, T))