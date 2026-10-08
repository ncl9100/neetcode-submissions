class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #convert array to set
        myset = set()
        for i in nums:
            myset.add(i)
        
        if len(myset) == 0:
            return 0
        
        max_sequence = 0
        curr_sequence = 0
        for i in nums:
            if i-1 not in myset:
                #doesn't have left neighbor, start of sequence
                curr_sequence = 1
                while i+curr_sequence in myset:
                    curr_sequence +=1
                if curr_sequence>max_sequence:
                    max_sequence = curr_sequence
        return max_sequence


        