class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        if len(intervals) == 0:
            return [newInterval]
        first = False
        start = False
        delete = [0]*len(intervals)
        for i in range(len(intervals)):
            if (newInterval[0] <= intervals[i][1] and newInterval[1] >= intervals[i][1]) or (newInterval[0] >= intervals[i][0] and newInterval[1] <= intervals[i][1]) or (newInterval[0] <= intervals[i][0] and newInterval[1] >= intervals[i][1]) or (newInterval[1] >= intervals[i][0] and newInterval[0] <= intervals[i][0]):
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
                start = True
                intervals[i] = newInterval
                if not first:
                    first = True
                else:
                    delete[i-1] = 1
            else:
                if start:
                    break
        res = []
        if not first:
            idx = 0
            for i in range(len(intervals)):
                if intervals[i][1] <= newInterval[0]:
                    idx = i
            delete[idx] = 2
            if newInterval[1] <= intervals[0][0]:
                res.append(newInterval)
                delete[idx] = 0
        for i in range(len(intervals)):
            if delete[i] == 0:
                res.append(intervals[i])
            if delete[i] == 2:
                res.append(intervals[i])
                res.append(newInterval)
        return res
