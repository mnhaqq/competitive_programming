class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        count = 0
        len_s = len(s)

        i = 0
        while i < len_s:
            if s[i] == letter:
                count +=1
            i+=1
        percentage = (count/len_s) * 100
        return int(percentage // 1)