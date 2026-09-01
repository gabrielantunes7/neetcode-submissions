class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count, t_count = {}, {}
        for c_s in s:
            s_count[c_s] = s_count.get(c_s, 0) + 1
        for c_t in t:
            t_count[c_t] = t_count.get(c_t, 0) + 1
        if s_count == t_count:
            return True
        return False