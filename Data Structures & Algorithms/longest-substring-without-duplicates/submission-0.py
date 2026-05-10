class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = ""
        maxlength = 0

        for c in s:
            if (c in substring):
                substring = substring[substring.index(c) + 1:]

            substring += c
            maxlength = max(maxlength, len(substring))
                
        return maxlength