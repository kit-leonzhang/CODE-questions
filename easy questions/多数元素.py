def majorityElement(nums: list) -> int:
    nums.sort()
    return nums[len(nums)//2]

def majorityElement2(nums) -> int:
    cur = nums[0]
    count = 0
    for _ in nums:
        if cur == _:
            count += 1
        else:
            count -= 1
            if count == 0:
                cur = _
                count = 1

    return cur

def majorityElement3(nums) -> int:
    dic = {}
    set1 = set(nums)
    for i in nums:
        dic[i] = dic.get(i, 0) + 1
    for i in set1:
        if dic.get(i) > (len(nums) // 2):
            return i