from collections import OrderedDict

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic = OrderedDict()

        for i in range(len(order)):
            dic[order[i]] = i

        for i in range(0, len(words)-1):
            curr_idx = len(words[i])
            next_idx = len(words[i+1])
            p1 = p2 = 0
            while p2 < curr_idx and p1 < next_idx:
                if dic[words[i][p1]] > dic[words[i+1][p2]]:
                    return False
                if dic[words[i][p1]] < dic[words[i+1][p2]]:
                    break
                p1+=1
                p2+=1
            if p1 == next_idx and p2 < curr_idx:
                return False        
        return True