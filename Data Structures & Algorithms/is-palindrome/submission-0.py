class Solution:
    def isPalindrome(self, s: str) -> bool:
    
    
      
        
        def is_alphanumeric(ch):
            ascii_value=ord(ch)
            return (ord('A')<=ascii_value<=ord('Z') or
            ord('a')<=ascii_value<=ord('z')or
            ord('0')<=ascii_value<=ord('9'))

        def to_lowercase(ch):
            if ('A')<=ch<=('Z'):
                return chr(ord(ch)+32)  # converts to lowercase
            return ch
        filtered=[]
        for ch in s:
            if is_alphanumeric(ch):
                filtered.append(to_lowercase(ch))

        start=0;end=len(filtered)-1 
        while start<end:
            if filtered[start]!=filtered[end]:
                return False
            start+=1
            end-=1
        return True


      

        