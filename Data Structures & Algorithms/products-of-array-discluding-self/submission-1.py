class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a = [1] * len(nums)
        left = 1
        right = 1
        for i in range(len(nums)):
            a[i] = left
            left = left*nums[i]
        for i in range(len(nums)-1,-1,-1):
            a[i] *= right
            right *= nums[i]
        return a