class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        
        while l < r:
            # Added l < r bound check and changed s[1] to s[l]
            while l < r and not self.alphaNum(s[l]):
                l += 1
            # Added l < r bound check and fixed self. typo
            while l < r and not self.alphaNum(s[r]):
                r -= 1
                
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
            
        return True
    
    def alphaNum(self, c):
        # Wrapped in outer parentheses to fix the syntax error
        return (
            (ord('A') <= ord(c) <= ord('Z')) or
            (ord('a') <= ord(c) <= ord('z')) or
            (ord('0') <= ord(c) <= ord('9')) # Fixed 'e' to '0'
        )