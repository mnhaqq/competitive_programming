class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_string = ""
        len_word1 = len(word1)
        len_word2 = len(word2)

        i = 0
        while i < len_word1 + len_word2:
            if i < len_word1 and i < len_word2:
                new_string += word1[i]
                new_string += word2[i]
            elif i < len_word1:
                new_string += word1[i]
            elif i < len_word2:
                new_string += word2[i]
            i+=1
        return new_string