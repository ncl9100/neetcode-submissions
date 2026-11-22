class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = Counter(s)
        t_dict = Counter(t)

        if len(s) != len(t):
            return False
        for char in s:
            freq_s = s_dict[char]
            if char in t_dict and t_dict[char] == freq_s:
                continue
            else:
                return False
        return True
                
            

        