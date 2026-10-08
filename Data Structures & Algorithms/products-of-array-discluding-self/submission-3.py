class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        suffix = [0] * len(nums)
        product = 1
        for i in range(len(prefix)):
            if i > 0:
                prefix[i] = nums[i-1] * product
                product = product * nums[i-1]
            else:
                prefix[i] = product
        print(prefix)

        product = 1
        for j in range(len(suffix) - 1, -1, -1):
            if j < len(suffix) - 1:
                suffix[j] = nums[j+1] * product
                product = product * nums[j+1]
            else:
                suffix[j] = product
        print(suffix)
        for i in range(len(nums)):
            prefix[i] = prefix[i] * suffix[i]

        return prefix

        