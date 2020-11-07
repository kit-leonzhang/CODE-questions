def merge(nums1: list, m: int, nums2: list, n: int) -> None:
    start = 0
    end = m
    if m == 0:
        for k in range(n):
            nums1.insert(k, nums2[k])
            nums1.pop()
    else:
        for i in range(n):
            for j in range(start, end):
                if nums2[i] <= nums1[j]:
                    nums1.insert(j, nums2[i])
                    nums1.pop()
                    start = j+1
                    end += 1
                    break
                elif nums2[i] > nums1[end-1]:
                    nums1.insert(end, nums2[i])
                    nums1.pop()
                    start = end
                    end += 1
                    break



if __name__ == "__main__":
    Nums1 = [0]
    m1 = 0
    Nums2 = [1]
    n2 = 1
    ##m1 = 0
    #Nums2 = [1]
    #n2 = 1
    merge(Nums1, m1, Nums2, n2)
    print(Nums1)
