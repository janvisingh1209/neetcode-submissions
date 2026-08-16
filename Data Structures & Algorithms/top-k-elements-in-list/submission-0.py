class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

     # create a dictionary to map frequency and the elements corresponding to that frequency 
        
        freq_map={}

        for num in nums:
            freq_map[num]=freq_map.get(num,0)+1
            #creates a dictionary with num and freq 

            #now we create a bucket where frequency=index
        n=len(nums)  
        buckets=[[] for _ in range(n+1)]
            
        for num,freq in freq_map.items():
            buckets[freq].append(num) #append the num corresponding to the freq if 3 occurs twice then in bucket 2 we will add 3
             # now the buckets are filled

        res=[] #creates a list
        for freq in range(n,0,-1): #checks frequency in descending order
            for num in buckets[freq]:
                res.append(num)
                if len(res)==k:
                    return res



