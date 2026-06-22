class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_dict ={}
        for char in s:
            if char not in char_dict:
                char_dict[char] = 0
            char_dict[char] +=1
        
        for char in t:
            if char not in char_dict:
                return False
            char_dict[char] -= 1

        for count in char_dict.values():
            if count != 0:
                return False
                
        return True
