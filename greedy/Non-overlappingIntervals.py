class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        intervals = sorted(intervals)
        res = 0
        last = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[last][1]:
                res += 1
                if intervals[i][1] >= intervals[last][1]:
                    continue
                else:
                    last = i
            else:
                last = i
        return res
