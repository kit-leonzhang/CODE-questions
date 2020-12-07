def twoSum(numbers: list, target: int) -> list:
    start = 0
    end = len(numbers) - 1
    #for i in range(len(numbers)):
    #    if numbers[i] > target:
    #        end = i
    #        break
    for k in range(start, end + 1):
        if numbers[start] + numbers[end] == target:
            return [start + 1, end + 1]
        if numbers[start] + numbers[end] < target:
            start += 1
            if end <= start:
                break
            continue
        if numbers[start] + numbers[end] > target:
            end -= 1
            if end <= start:
                break
            continue
    return False


if __name__ == "__main__":
    N = [2, 3, 4]
    T = 6
    print(twoSum(N, T))