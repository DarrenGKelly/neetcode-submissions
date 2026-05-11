from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        maxLength = 0
        start = 0

        # Go through each char as the end pointer
        for i in range(len(s)):
            valid = False

            # Check that the current substring is valid, if not, move start pointer
            while(not valid and start != len(s)):
                count = Counter(s[start:i + 1])
                changes = 0

                for (char, num) in count.most_common()[1:]:
                    changes += num
                
                if (changes <= k):
                    maxLength = max(maxLength, len(s[start:i + 1]))
                    valid = True
                else:
                    start += 1

        return maxLength