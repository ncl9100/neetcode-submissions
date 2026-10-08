class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        myset = set()
        for i in nums:
            myset.add(i)
        #find min and max
        if len(myset) ==0:
            return 0
        min_val = min(myset)
        max_val = max(myset)
        longest_sequence = 0
        current_sequence = 0
        for i in range(min_val, max_val+1):
            if i in myset:
                current_sequence +=1
                if current_sequence > longest_sequence:
                    longest_sequence = current_sequence
            else:
                current_sequence = 0
        return longest_sequence

        