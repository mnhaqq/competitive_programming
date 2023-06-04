class Solution:
    def freqAlphabets(self, s: str) -> str:
        dic = dict()
        chars = "abcdefghijklmnopqrstuvwxyz"
        chars = [i for i in chars]

        digits = [str(i) for i in range(1,10)]
        temp = [str(i)+"#" for i in range(10,27)]
        digits += temp

        i = 0
        while i < 26:
            dic[digits[i]] = chars[i]
            i+=1

        new_s = []
        i = 0
        while i < len(s):
            if i < len(s) - 2 and s[i+2] == "#":
                new_s.append(s[i:i+3])
                i+=3
                continue
            else:
                new_s.append(s[i]) 
            i+=1

        final = ""
        for char in new_s:
            final+=dic.get(char)
        return final
        