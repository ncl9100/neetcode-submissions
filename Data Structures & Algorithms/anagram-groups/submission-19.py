class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freqArray = [0] * 26
        mymap = {}
        for i in range(0, len(strs)):
            for j in strs[i]:
                freqArray[ord(j)-ord('a')] +=1
            if tuple(freqArray) in mymap:
                mymap[tuple(freqArray)].append(strs[i])
            else:
                mymap[tuple(freqArray)] = [strs[i]]
            freqArray = [0] * 26
        
        result = []
        for i in mymap:
            result.append(mymap[i])
        return result



        