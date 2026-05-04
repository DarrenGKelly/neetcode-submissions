class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Option 2: join into a string first, then lower
        ns = ''.join(c for c in s if c.isalnum()).lower()
        return ns == ns[::-1]
