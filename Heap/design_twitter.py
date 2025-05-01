# https://neetcode.io/problems/design-twitter-feed

class Twitter:

    def __init__(self):
        self.followmap = defaultdict(set)
        self.tweetmap = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweetmap[userId].append([self.time, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        users = self.followmap[userId]
        users.add(userId)
        list_of_tweets = [[tweet[0],tweet[1]] for user in users for tweet in self.tweetmap[user]]
        return_list = []
        for i in range(0, len(list_of_tweets)):
            if i<10:
                heapq.heappush(return_list, list_of_tweets[i])
            else:
                if list_of_tweets[i][0]>return_list[0][0]:
                    heapq.heappop(return_list)
                    heapq.heappush(return_list, list_of_tweets[i])
        p = []
        while len(return_list):
            p.append(heapq.heappop(return_list)[1])
        return p[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followmap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followmap[followerId].discard(followeeId)

# time complexity of postTweet is O(1)
# time complxity of getnewsfeed is O(n*k*log10) where n is the number of tweets/user and k is the number of users
# time complexity of follow is O(1)
# time complexity of unfollow is O(1)
# space complexity is O(n) where n is the number of tweets
# space complexity of getnewsfeed is O(n*k) where n is the number of tweets/user and k is the number of users
# space complexity of follow is O(n)
# space complexity of unfollow is O(n)