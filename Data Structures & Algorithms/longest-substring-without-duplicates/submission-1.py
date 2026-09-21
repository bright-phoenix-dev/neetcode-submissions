class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l, r = 0, 1
        max_unique_chars = len(set(s))
        window = set(s[l:r])
        max_length = len(window)
        while r < len(s):
            if s[r] in window:
                window.remove(s[l])
                l += 1
            else:
                window.add(s[r])
                r += 1
            max_length = max(max_length, len(window))
            if max_length == max_unique_chars:
                break
        return max_length