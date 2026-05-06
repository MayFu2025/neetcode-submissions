class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): # If the lengths are different you know they aren't anagrams
            return False
        
        set_s = {}
        set_t = {}

        for let in s:
            if let in set_s:
                set_s[let] += 1
            else:
                set_s[let] = 1
        
        for let in t:
            if let in set_t:
                set_t[let] += 1
            else:
                set_t[let] = 1
        
        return set_s == set_t
