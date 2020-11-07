def plusOne(digits: list) -> list:
    lens = len(digits)
    sum = 0
    result = []
    for i in range(lens):
        sum += digits[lens-i-1]*(10**i)
    if sum == 0:
        result = [0] * (lens - 1)
        result.append(1)
        return result
    else:
        sum += 1
        for j in str(sum):
            result.append(int(j))
        return result



if __name__ == "__main__":
    #N = [1, -2, 3, 4]
    N = [0, 0, 0]
    print(plusOne(N))
