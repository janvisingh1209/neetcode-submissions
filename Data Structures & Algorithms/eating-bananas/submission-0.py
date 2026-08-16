class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start=1 #start with one banana 
        end=max(piles) #range extends till the max number of ban that can be eaten in an hour
        while start<end:
            mid=(start+end)//2 #narrows range using b.s
            hours=0
            for pile in piles:
                hours+=(pile+mid-1)//mid #no. of hours taken to devour each pile in total
                
            if hours<=h:  #within range try to find smaller k 
                end=mid
            else:
                start=mid+1
        return start

        #tc=  N.OlogM
        #sc= O(1)
