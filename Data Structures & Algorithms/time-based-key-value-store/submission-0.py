class TimeMap:

    def __init__(self):
        self.store={} #initialize a dictionary to store keys with corresponding keys and timestamp,values
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key]=[]
        self.store[key].append((timestamp,value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        arr=self.store[key]
        res=""
        start=0
        end=len(arr)-1

        while start<=end:
            mid=(start+end)//2
            if arr[mid][0]<=timestamp:
                res=arr[mid][1]
                start=mid+1
            else:
                end=mid-1
        return res









        
