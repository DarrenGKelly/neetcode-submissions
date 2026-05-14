class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end = 0, 0
        hashset = set()

        for c in s:
            if (len(set(s[start: end + 1])) != end - start + 1):
                start += 1

            end += 1

        return end - start
            