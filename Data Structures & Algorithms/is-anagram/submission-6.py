class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        S = {}
        T = {}
        for i in s:
            if i not in S:
                S[i] = 1
            else:
                S[i] += 1
        for i in t:
            if i not in T:
                T[i] = 1
            else:
                T[i] += 1
        return S == T
