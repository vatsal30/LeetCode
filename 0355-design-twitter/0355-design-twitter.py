from collections import defaultdict
import heapq
class Twitter:

    def __init__(self):
        self.users = defaultdict(set)
        self.posts = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.users[userId].add(userId)
        self.posts[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        recentTweet = []
        for followerId in self.users[userId]:
            if self.posts[followerId]:
                lastPost = self.posts[followerId][-1]
                heapq.heappush(recentTweet, (-lastPost[0], lastPost[1], followerId, len(self.posts[followerId])-1))
        count = 0
        while count < 10 and recentTweet:
            _, tweet, owner, tweetIdx = heapq.heappop(recentTweet)
            if tweetIdx > 0:
                tweetIdx -= 1
                post = self.posts[owner][tweetIdx]
                heapq.heappush(recentTweet, (-post[0], post[1], owner, tweetIdx))
            feed.append(tweet)
            count += 1
        return feed
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.users[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)