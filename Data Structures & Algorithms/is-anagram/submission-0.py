class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counts = {}
        for l_s, l_t in zip(s,t):
            counts[l_s] = counts.get(l_s, 0) + 1
            counts[l_t] = counts.get(l_t, 0) - 1

        return all(val == 0 for val in counts.values())