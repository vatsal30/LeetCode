from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.user = defaultdict(set)
        self.tweet = defaultdict(list)
        self.time = 0
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweet[userId].append((self.time, tweetId))
        if userId not in self.user[userId]:
            self.user[userId].add(userId)

    def getNewsFeed(self, userId: int) -> List[int]:
        recentTweet = []
        for followerId in self.user[userId]:
            if self.tweet[followerId]:
                last_idx = len(self.tweet[followerId]) - 1
                last_tweet = self.tweet[followerId][last_idx]
                recentTweet.append((-last_tweet[0], last_tweet[1], followerId, last_idx))
        heapq.heapify(recentTweet)
        cnt = 0
        ans = []
        while cnt < 10 and recentTweet:
            _, tweet_id, follower_id, idx = heapq.heappop(recentTweet)
            if idx > 0:
                idx -= 1
                tweet = self.tweet[follower_id][idx]
                heapq.heappush(recentTweet, (-tweet[0], tweet[1], follower_id, idx))
            ans.append(tweet_id)
            cnt += 1
        return ans


    def follow(self, followerId: int, followeeId: int) -> None:
        self.user[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return 
        if followeeId in self.user[followerId]:
            self.user[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)