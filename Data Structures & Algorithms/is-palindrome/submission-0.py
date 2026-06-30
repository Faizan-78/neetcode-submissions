class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = ''.join(c for c in s if c.isalnum())
        s = s.strip()
        if s == s[::-1]:
            return True
        return False