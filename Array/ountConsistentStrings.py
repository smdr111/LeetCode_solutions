class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set(allowed)
        count = 0

        for w in words:
            ok = True
            for ch in w:
                if ch not in allowed_set:
                    ok = False
                    break
            if ok:
                count += 1

        return count

