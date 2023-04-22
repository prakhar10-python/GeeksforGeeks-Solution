class Solution:
    def romanToInt(self, s: str) -> int:
        dictonary = {"I": 1,"V": 5,"X": 10,"L": 50,"C": 100,"D": 500,"M": 1000}
        l1 = [dictonary[i] for i in s]
        l1.reverse()
        num = 0
        for idx, i in enumerate(l1):
            if idx == 0:
                num += i
            elif i < l1[idx - 1]:
                num = num - i
            else:
                num += i
        return num
s=input()
d=Solution()
ans=d.romanToInt(s)
print(ans)