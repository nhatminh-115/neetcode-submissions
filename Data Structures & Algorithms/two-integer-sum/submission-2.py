class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            temp = target - num
            if temp not in seen:
                pass #Note: ờ thì thật ra nếu không thấy thì skip chứ chả làm gì
            else: 
                return [seen[temp], i] #seen là dict, trace ngược bằng value thì ra key
                                       #Nhưng py không cho nên phải đảo ngược cặp id, i
            seen[num] = i
                