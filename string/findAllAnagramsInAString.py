class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        s_window = [0]*26
        p_window = [0]*26
        for j in range(len(p)):
            s_window[ord(s[j])-97] += 1
            p_window[ord(p[j])-97] += 1
        left = 0
        res = []
        if s_window == p_window:
            res.append(0)
        for right in range(len(p), len(s)):
            s_window[ord(s[left])-97] -= 1
            s_window[ord(s[right])-97] += 1
            left += 1
            if s_window == p_window:
                res.append(left)
        return res
