class Solution:
    def similarPairs(self, words: List[str]) -> int:
        words = [sorted(word) for word in words]
        words = [set(word) for word in words]

        num_pairs = 0
        i = 0
        while i < len(words)-1:
            j = i+1
            while j < len(words):
                if words[i] == words[j]:
                    num_pairs+=1
                j+=1
            i+=1
        return num_pairs