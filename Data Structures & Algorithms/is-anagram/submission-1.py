class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_arr={} #create a dictionary 
        
        if len(s)!= len(t):
            return False

        for char in s:
            if char in char_arr:
                char_arr[char]+=1
            else:
                char_arr[char]=1
        
        for char in t:
            if char in char_arr:
                char_arr[char]-=1

                if char_arr[char]<0: # if the count of char
                                    #becomes negative meaning that more number of a particular alphabet exists in t than in s hence value can become negative 
                    return False

            else:  
                return False # char in t is not in s 
        

        for count in char_arr.values():
            if count!=0: #checks if all the values of char count is 0 bcz there might br a case where s might have an alphabet ehich is not present in t in which case the function will return false without the last function that checks count==0 for all alphabets

                return False

        return True



    




                    












