class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        temp = {} #character là key, số lượng là value
        maxcount = 0
        count = 0
        left = 0

        for i in range(len(s)):
            temp[s[i]] = temp.get(s[i], 0) + 1 
            count = max(count, temp[s[i]])
            
            while (i - left + 1) - count > k:
                temp[s[left]] -= 1
                left += 1

            maxcount = max(maxcount, i - left + 1)

        return maxcount