class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = " ".join(s)
        s = s.split()
        t = " ".join(t)
        t = t.split()
        
        dic = dict()

        for char in s:
            dic[char] = dic.get(char, 0) + 1
        for char in t:
            dic[char] = dic.get(char, 0) + 1

        for key, value in dic.items():
            if value % 2 != 0:
                return key