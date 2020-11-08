def maxProfit(prices:list) -> int:
    lens = len(prices)
    sum = 0
    for i in range(lens-1):
        if prices[i] < prices[i+1]:
            sum += prices[i+1]-prices[i]
    return sum


if __name__ == "__main__":
    N = [7, 1, 5, 3, 6, 4]
    print(maxProfit(N))