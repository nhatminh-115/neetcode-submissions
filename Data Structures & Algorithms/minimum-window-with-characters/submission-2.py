class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = {}
        for i in t:
            target[i] = target.get(i, 0) + 1
            #là ra được cái dict chứa các chữ, số lượng (không thứ tự vì bài k yêu cầu)
        
        temp = {} #dict của window hiện tại
        left = 0 #cạnh trái win curr
        start = 0 # cạnh trái output
        required = len(target) #số loại chữ cần đủ (chưa xét số lượng)
                               #sau phải đủ số lượng (value) của key mới được so với required
        count = 0 #để so với required
        window = float("inf")

        for i in range(len(s)):
            temp[s[i]] = temp.get(s[i], 0) + 1
        
            if s[i] in target and temp[s[i]] == target[s[i]]:
                count += 1
            
            while count == required:
                if i - left + 1 < window:
                    window = i - left + 1
                    start = left

                temp[s[left]] -= 1 #Cắt bớt chữ bên trái (giảm 1 giá trị)

                if s[left] in target and temp[s[left]] < target[s[left]]:
                    count -= 1

                left += 1 #Cắt xong nếu không mất count thì đẩy window lên 1 số
        if window == float("inf"):
            return ""
        else:
            return s[start: start + window]