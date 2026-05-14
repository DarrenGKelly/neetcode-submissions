from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        count = Counter()
        maxCount = 0
        maxLength = 0
        start = 0

        # Go through each char as the end pointer
        for end in range(len(s)):
            count[s[end]] += 1
            maxCount = max(maxCount, count[s[end]])

            if (end - start + 1) - maxCount > k:
                count[s[start]] -= 1
                start += 1

            maxLength = max(end - start + 1, maxLength)


        return maxLength