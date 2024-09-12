class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_common_prefix = ""
        if len(strs) == 0 or len(strs[0]) == 0:
            return longest_common_prefix
                        
        i = 1
        shortest = len(strs[0])
        while i < len(strs):
            if len(strs[i]) < shortest:
                shortest = len(strs[i])
            i+=1

        i = 0
        while i < shortest:
            check = strs[0][i]
            j = 0
            while j < len(strs):
                if check != strs[j][i]:
                    return longest_common_prefix
                j+=1
            longest_common_prefix += check
            i+=1
        
        return longest_common_prefix