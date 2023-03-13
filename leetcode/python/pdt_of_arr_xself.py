#https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]*len(nums)

        prefix = 1
        for i in range(len(nums)):
            result[i] *= prefix
            prefix *= nums[i]
        
        length = len(nums)
        postfix = 1
        for i in range(length):
            result[length-i-1] *= postfix
            postfix *= nums[length-i-1]
        return result