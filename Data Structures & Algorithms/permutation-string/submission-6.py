from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        start = 0

        for i in range(len(s2) - len(s1) + 1):
            comparison = s2[start:len(s1) + i]

            if (Counter(comparison) == Counter(s1)):
                return True
            else:
                start += 1
            
        return False