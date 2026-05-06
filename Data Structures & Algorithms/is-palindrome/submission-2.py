class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "").lower() # Remove all spaces, make everything lowercase
        print(s)
        s = re.sub(r'[^a-zA-Z0-9]', '', s) # Remove all non-alphanumeric characters
        
        left = 0 # left index pointer
        right = len(s) - 1 # right index pointer

        while left <= right:            
            if s[left] != s[right]:
                return False
            else: # Shift the pointers
                left += 1
                right -= 1
        
        return True

        