class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):  #check if s1 is greater than s2
            return False

        s1_count=Counter(s1)  #counter for s1
        window_count=Counter(s2[:len(s1)]) #counter for s2 of window length=s1

        if window_count==s1_count: #check if initially window len char count matches count of s1
            return True
        for i in range(len(s1),len(s2)):  # if not traverse elements after len(s1) one by one
            window_count[s2[i]]+=1  #increment count of new element
            window_count[s2[i-len(s1)]]-=1   # decrement count of first index (0)
            
            if window_count[s2[i-len(s1)]]==0:  
                del window_count[s2[i-len(s1)]]#for an efficient structure

            if window_count==s1_count:    #final check 
                return True
        return False
            






        