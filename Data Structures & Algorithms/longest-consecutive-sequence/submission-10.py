class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        myset = set()
        for i in nums:
            myset.add(i)

        if len(myset) ==0:
            return 0

        longest_sequence = 0
        current_sequence = 0
        for i in nums:
            #check left neighbor
            if i-1 not in myset: #start of sequence
                current_sequence =1
                while i + current_sequence in myset:
                    current_sequence +=1
                if current_sequence > longest_sequence:
                    longest_sequence = current_sequence

        return longest_sequence

        