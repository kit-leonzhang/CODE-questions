def maxProfit(prices: list) -> int:
    if not prices or len(prices) == 1:
        return 0
    start = 0
    gain = 0
    for i in range(start + 1, len(prices)):
        if prices[start] > prices[i]:
            start = i
        else:
            gain = max(gain, prices[i] - prices[start])
        if start == len(prices) - 1:
            break
    return gain


if __name__ == "__main__":
    N = [7, 1, 5, 3, 6, 4]
    print(maxProfit(N))
