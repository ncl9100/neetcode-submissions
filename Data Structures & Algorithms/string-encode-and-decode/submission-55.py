class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for i in range(0, len(strs)):
            result = result + str(len(strs[i])) + '#' + strs[i]
        
        return result

    def decode(self, s: str) -> List[str]:
        j = 0
        result = []
        s1=""
        lenn=0
        while j<len(s):
            while s[j]!='#':
                s1 +=s[j]
                j+=1
            lenn = int(s1)
            result.append(s[j+1: j+1+lenn])
            j+=lenn+1
            s1=""

            
        return result