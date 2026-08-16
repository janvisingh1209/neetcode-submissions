from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""   #empty string

        #create two lists
        size, res = [], ""    # example: ["hello","jan"]

        for s in strs:
            size.append(len(s)) # consists of list like [4,3]

        for sz in size:
            res += str(sz)   #convert length like 4 to "4"
            res += ','

        res += '#'      #add hash to separate length from actual string that we will add

        for s in strs:
            res += s
        return res    #we get res="4,3,#hellojan"

    def decode(self, s: str) -> List[str]:
        # the string that we created by encoding will now be traversed

        if not s:   #if list is empty
            return []

        sizes, res, i = [], [], 0

        # here str="4,3#hellojan"
        while s[i] != '#':
            cur = ""   # stores length of each string temporarily 
            while s[i] != ',':
                cur += s[i]
                i += 1
            sizes.append(int(cur))  #appends the length "4" as 4
            i += 1  # i points to #
        i += 1   # so that now i points to h

        for sz in sizes:
            res.append(s[i:i + sz])   #now i points to the actual string
            i += sz
        return res



