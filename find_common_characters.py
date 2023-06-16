class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        alphabets = [0] * 26

        for char in words[0]:
            alphabets[ord(char)-97]+=1

        words = [" ".join(word) for word in words]
        words = [word.split() for word in words]

        for i in range(1, len(words)):
            for j in range(len(words[i])):
                count = words[i].count(words[i][j])
                if count == alphabets[ord(words[i][j])-97] or count == 0:
                    continue
                elif count < alphabets[ord(words[i][j])-97]:
                    alphabets[ord(words[i][j])-97] = count

        for i in range(len(alphabets)):
            for j in range(len(words)):
                if chr(i+97) not in words[j]:
                    alphabets[i] = 0
                    break
        final = []
        for i in range(len(alphabets)):
            while alphabets[i] > 0:
                final.append(chr(i+97))
                alphabets[i]-=1
        return final
