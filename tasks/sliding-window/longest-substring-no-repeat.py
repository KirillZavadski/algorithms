from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        symbols = deque()
        check = set()
        max_len = 0
        for i in range(len(s)):
            while s[i] in check:
                deleted = symbols.popleft()
                check.remove(deleted)
                
            check.add(s[i])
            symbols.append(s[i])
            if len(check) > max_len:
                max_len = len(check)
        return max_len