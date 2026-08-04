class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        a = set(nums)
        maxstreak = 0
        for i in a:
            if i-1 not in a:
                streak = 1
                temp = i
                while i+1 in a:
                    streak += 1
                    i += 1
                maxstreak =  max(maxstreak, streak)
        return maxstreak