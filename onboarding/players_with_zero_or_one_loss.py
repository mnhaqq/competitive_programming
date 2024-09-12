class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        wins = dict()
        losses = dict()

        for winner, loser in matches:
            wins[winner] = wins.get(winner, 0) + 1
            losses[loser] = losses.get(loser, 0) + 1

        no_losses = [i for i in wins if i not in losses]
        one_loss = [i for i in losses if losses[i] == 1]

        return [sorted(no_losses), sorted(one_loss)]