class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        def HR1(arr):
            k = len(arr)
            if len(arr) == 1:
                return arr[0]
            
            dp = [0] * k

            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])

            for i in range(2, k):
                dp[i] = max(dp[i-1], dp[i-2]+ arr[i])
            
            return dp[-1]
        
        return max(HR1(nums[1:]), HR1(nums[:-1]))