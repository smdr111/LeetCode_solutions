class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_index = {}  # son -> oxirgi ko‘ringan indeks
        for i, x in enumerate(nums):
        # Agar x oldin uchragan bo‘lsa
            if x in last_index:
            # Indekslar orasidagi masofa k dan kichik/ tengmi?
                if i - last_index[x] <= k:
                    return True

        # Har doim oxirgi indeksni yangilab boramiz
            last_index[x] = i

        return False
        
        
