class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [0] * len(nums)
        right = [0] * len(nums)
        product = 1
        for i in range(len(left)):
            if i > 0:
                left[i] = nums[i-1] * product
                product = product * nums[i-1]
            else:
                left[i] = product
        print(left)

        product = 1
        for j in range(len(right) - 1, -1, -1):
            if j < len(right) - 1:
                right[j] = nums[j+1] * product
                product = product * nums[j+1]
            else:
                right[j] = product
        print(right)
        for i in range(len(nums)):
            left[i] = left[i] * right[i]
        return left

        