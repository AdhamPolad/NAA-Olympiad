class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key = lambda x : (x[0], -x[1]))
        
        res = 0
        ending = 0
        
        for _, end in intervals:
            if end > ending:
                res += 1
                ending = end
        
        return res