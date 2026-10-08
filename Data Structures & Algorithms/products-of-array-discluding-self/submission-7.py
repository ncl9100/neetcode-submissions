class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #create prefix array
        #create postfix aray
        #multiply the products for each i
        prefix = [1] * len(nums)
        prefix_product = 1
        for i in range(len(nums)):  
            if(i==0):
                prefix[i] = 1
            else:
                prefix[i] = prefix_product 
            prefix_product = prefix_product * nums[i]
        postfix = [1]*len(nums)
        postfix_product = 1
        for i in range(len(nums)-1, -1, -1):
            if(i==len(nums)-1):
                postfix[i] = 1
            else:
                postfix[i] = postfix_product 
            postfix_product = postfix_product * nums[i]
        for i in range(0, len(nums)):
            nums[i] = prefix[i]*postfix[i]
        return nums


        