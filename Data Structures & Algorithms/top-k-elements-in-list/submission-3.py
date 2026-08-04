class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1
        return sorted(seen, key = lambda num: seen[num], reverse = True)[:k]
                #ở đây là return seen (key), nhưng sort theo key = seen[num] = value.