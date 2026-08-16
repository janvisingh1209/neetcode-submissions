class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        #we increment and decrement length of window and match freq using counter
        
        l=0
        res = [float("inf"), 0, 0] # initializing window length
        have=0
        t_count=Counter(t)#counts freq of chars in t
        need = len(t_count)  #need substring with all t chars
        
        window_count= {}

        for r in range(len(s)):
            char=s[r]

            window_count[char]=window_count.get(char, 0) + 1 #increments count of char in s
            if char in t_count and window_count[char]==t_count[char]:
                have+=1
            while have==need:
                if (r - l + 1) < res[0]:
                    res = [r - l + 1, l, r]
                window_count[s[l]] -= 1
                if s[l] in t_count  and window_count[s[l]] < t_count[s[l]]:
                    have-=1
                l+=1

        l, r = res[1], res[2]
        return s[l:r+1] if res[0] != float("inf") else ""













        