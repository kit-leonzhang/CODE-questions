# def twosum(nums, target):
#    n = len(nums)
#    for i in range(n):
#        for j in range(i + 1, n):
#            if nums[i] + nums[j] == target:
#                return [i, j]


def twosum(nums, target):
    #lens = len(nums)
    #j = -1
    #for i in range(1, lens):
    #    temp = nums[:i]
    #    if (target - nums[i]) in temp:
    #        j = temp.index(target - nums[i])
    #        break
    #if j >= 0:
    #    return [j, i]
        
        
        d = {}
        n = len(nums)
        for x in range(n):
            if target - nums[x] in d:
                return d[target-nums[x]],x
            else:
                d[nums[x]] = x


if __name__ == "__main__":
    N = [2, 7, 11, 15]
    T = 9
    print(twosum(N, T))
