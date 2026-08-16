class Twitter:

    def __init__(self):
        self.time=0
        self.tweets=defaultdict(list) # create a list of user as key and the values being the timestamp and tweetid as tupple values  {1:(1,101), 2:(3,202)}
        self.following=defaultdict(set)  # create a dict in form of set to prevent duplicate values,it holds followee for each followers including themselves

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time+=1
        self.tweets[userId].append((self.time,tweetId))  # use append cz its a list
        self.following[userId].add(userId)  # use add cz its a set
        

    def getNewsFeed(self, userId: int) -> List[int]:
        heap=[]
        result=[]
        for user in self.following[userId]:  # iterate over tweets of the users followed by given userid not any other id
            if self.tweets[user]:
                time,tweetId=self.tweets[user][-1] # push most recent tweet
                index=len(self.tweets[user])-1
                heapq.heappush(heap,(-time,tweetId,user,index))
        while heap and len(result)<10:
            _,tweetId,user,idx=heapq.heappop(heap)
            result.append(tweetId)
            if idx>0:
                time,tweetId=self.tweets[user][idx-1]
                heapq.heappush(heap,(-time,tweetId,user,idx-1))
        return result


        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId!=followeeId: # one cant unfollow themselves
        
            self.following[followerId].discard(followeeId)
        
