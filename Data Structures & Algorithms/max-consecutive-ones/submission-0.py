class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        curr = 0
        for i in range(0, len(nums)):
            if nums[i] == 1:
                curr+=1
                ans = max(curr, ans)
            else:
                curr=0
        return ans

        