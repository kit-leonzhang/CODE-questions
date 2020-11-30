class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        else:
            a = 1
            b = 2
            s = 0
            for i in range(3, n+1):
                s = a + b
                a = b
                b = s
            return s


if __name__ == "__main__":
    N = 4
    S = Solution()
    print(S.climbStairs(N))