class Solution:
    """"
#    def countAndSay(self, n: int) -> str:
#        if n == 1:
#            return "1"
#        else:
#            a = list(self.countAndSay(n-1))
#            i = 0
#            j = 0
#            for i in range(i+j, len(a)):
                b = []
                if i == len(a) - 1:
                    b.append(1)
                    b.append(a[len(a)-1])
                else:
                    for j in range(1, len(a)-i):
                        if a[i] != a[i+j]:
                            b.append(j)
                            b.append(a[i])
                            break
                        if i+j == len(a)-1:
                            b.append(j+1)
                            b.append(a[i])
                            break
            return ''.join([str(x) for x in b])
    """
    def countAndSay(self, n: int) -> str:
        now = "1"
        for _ in range(1, n):
            pre = now
            now = ""
            start = 0
            end = 0
            while end < len(pre):
                while (end < len(pre)) and (pre[start] == pre[end]):
                    end += 1
                now += str(end-start) + pre[start]
                start = end
        return now


if __name__ == "__main__":
    S = Solution()
    print(S.countAndSay(6))
