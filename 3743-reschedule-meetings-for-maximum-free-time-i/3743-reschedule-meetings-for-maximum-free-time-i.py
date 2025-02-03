class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        freeTimes = []
        for i in range(len(startTime)):
            if i == 0:
                freeTimes.append(startTime[i] - 0)
            else:
                freeTimes.append(startTime[i] - endTime[i-1])
        freeTimes.append(eventTime - endTime[i])
        ans = sum(freeTimes[:k+1])
        tmp = ans
        for i in range(1, len(freeTimes) - k):
            tmp = tmp - freeTimes[i - 1] + freeTimes[i + k]
            ans = max(ans, tmp)
        return ans        


                