class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        new=""
        
        for char in s:
            if char.isalnum():
                new+=char
        
        if new==new[::-1]:
            return True
        else:
            return False
