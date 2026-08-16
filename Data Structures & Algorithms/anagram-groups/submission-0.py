class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #create a hashmap

        anagram_map= defaultdict(list) #creates a dictionary

        for word in strs:
            key=''.join(sorted(word)) #creates a key by sorting the word ate becomes aet
            anagram_map[key].append(word) #add the word you just sorted according to the key for anagrams they key will remain same and hence each of the anagram will be appended as a value corresponding to that one particular key


        return list(anagram_map.values())