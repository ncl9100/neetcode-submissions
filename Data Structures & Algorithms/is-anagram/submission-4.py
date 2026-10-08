class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #create 2 hashmaps (hashtables)
        #compare frequencies (Values) for each hashtable key
        if(len(s)!=len(t)):
            return False
        table1 = {}
        table2 = {}
        for char in s:
            if char in table1:
                table1[char] +=1
            else:
                table1[char] = 1
        for char in t:
            if char in table2:
                table2[char] +=1
            else:
                table2[char] = 1
        
        for i in table1:
            if(i in table2):
                if(table1[i]!=table2[i]):
                    return False
            else:
                return False
        return True

        
        