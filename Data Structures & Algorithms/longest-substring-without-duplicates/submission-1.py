class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxcount = 0
        temp = set()
        count = 0
        left = 0

        for i in range(len(s)):
            while s[i] in temp:
                temp.remove(s[left])
                left += 1
            temp.add(s[i])
            count = i - left + 1
            maxcount = max(count, maxcount)
        return maxcount