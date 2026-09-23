class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        intervals = sorted(intervals)
        res = 0
        new = []
        new.append(intervals[0])
        act = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < new[act][1]:
                res += 1
                if intervals[i][1] >= new[act][1]:
                    continue
                else:
                    new[act] = intervals[i]
            else:
                new.append(intervals[i])
                act += 1
        return res
