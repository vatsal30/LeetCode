from bisect import bisect_left
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        pairs = []
        lp = len(potions)
        for spell in spells:
            potion_val = ceil(success / spell)
            idx = bisect_left(potions, potion_val)
            pairs.append(lp-idx)
        return pairs

        