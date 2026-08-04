class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = collections.defaultdict(list)
        for word in strs:
            key = "".join(sorted(word))
            a[key].append(word)
        return list(a.values())