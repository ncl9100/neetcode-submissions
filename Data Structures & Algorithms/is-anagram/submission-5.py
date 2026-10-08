class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #create 2 hashmaps (hashtables)
        #compare frequencies (Values) for each hashtable key
        if(len(s)!=len(t)):
            return False
        table1 = {}
        table2 = {}
        for i in range(0, len(s)):
            table1[s[i]] = 1+table1.get(s[i], 0)
            table2[t[i]] = 1+table2.get(t[i], 0)
        
        for i in table1:
            if table1[i] != table2.get(i, 0):
                return False
        return True

        
        