class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        player1 = 0
        player2 = 0
        left = 0
        right = len(piles) - 1
        while left < right:
            if piles[left] >= piles[right]:
                player1 += piles[left]
                player2 += piles[right]
            else:
                player1 += piles[right]
                player2 += piles[left]
            left += 1
            right -= 1
        return player1 > player2
        
