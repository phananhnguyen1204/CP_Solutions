class TweetCounts:
    # need to calculate how many chunks in [startTime, endTime] -> (endTime - startTime) // hour + 1

    def __init__(self):
        self.freq = {
            "minute": 60,
            "hour": 3600,
            "day": 86400
        }
        # store timestamp of each sweets
        self.tweets = defaultdict(list)
        

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.tweets[tweetName].append(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        chunks = (endTime - startTime) // self.freq[freq] + 1
        print(self.freq[freq])
        res = [0] * chunks
        for t in self.tweets[tweetName]:
            chunk_idx = (t - startTime) // self.freq[freq]
            if startTime <= t <= endTime:
                res[chunk_idx] += 1
        return res


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)