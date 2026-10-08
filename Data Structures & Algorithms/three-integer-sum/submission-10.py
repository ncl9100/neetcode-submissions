class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_sorted = sorted(nums)

        result = []
        i=0
        while i<len(nums_sorted)-1 and nums_sorted[i] <=0:
            curr_element = nums_sorted[i]
            complement = -nums_sorted[i]
            left = i+1
            right = len(nums_sorted)-1
            while left<right:
                summ = nums_sorted[left] + nums_sorted[right]
                if summ > complement:
                    right -=1
                elif summ < complement:
                    left+=1
                else:
                    result.append([curr_element, nums_sorted[left], nums_sorted[right]])
                    left+=1
                    right-=1
                    while left < right and nums_sorted[left] == nums_sorted[left - 1]:
                        left += 1
            i+=1
            while i<len(nums_sorted) and nums_sorted[i] == nums_sorted[i-1]:
                i+=1
        return result



        
        
        
        