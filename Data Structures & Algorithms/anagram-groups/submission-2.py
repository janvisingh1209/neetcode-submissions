class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups={}
        for word in strs:
            key=(tuple(sorted(Counter(word).items())))
            if key not in groups:
                groups[key]=[]
            groups[key].append(word)
        return list(groups.values())
        