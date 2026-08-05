class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = {}
        for char in t:
            target[char] = target.get(char, 0) + 1

        temp = {} #Đây là cái window nè
        left = 0 #Cạnh trái window
        count = 0                 # có bao nhiêu loại chữ đã đủ số lượng
        required = len(target)    # tổng số loại chữ cần đủ

        start = 0 #Cạnh trái của output
        min_length = float("inf") #infinite

        for i in range(len(s)):
            temp[s[i]] = temp.get(s[i], 0) + 1

            # Ví dụ t cần A:2, khi temp có đủ A:2 thì mới count += 1
            if s[i] in target and temp[s[i]] == target[s[i]]:
                count += 1 #Đã đủ 1 chữ, nếu chưa = required thì quét tiếp

            # Nếu Window hiện tại đã chứa đủ t
            while count == required:
                # Lưu nếu nó ngắn hơn đáp án cũ
                if i - left + 1 < min_length:
                    start = left #Lưu cạnh trái
                    min_length = i - left + 1 #Lưu kích thước

                # Thử bỏ ký tự bên trái để window ngắn lại
                temp[s[left]] -= 1

                # Nếu bỏ đi khiến thiếu một ký tự cần thiết
                if s[left] in target and temp[s[left]] < target[s[left]]:
                    count -= 1 #out while, cái min_length hợp lệ cuối cùng giữ nguyên

                left += 1

        if min_length == float("inf"):
            return ""

        return s[start:start + min_length]