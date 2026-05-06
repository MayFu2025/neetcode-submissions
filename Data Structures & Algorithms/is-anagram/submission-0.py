class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            for let in s:
                if s.count(let) != t.count(let):
                    return False
            return True
        else:
            return False
        