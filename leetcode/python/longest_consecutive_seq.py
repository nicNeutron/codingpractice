# https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numsSet = set(nums)

        maxCount = 0
        for i in numsSet:
            count = 0
            if (i-1) not in numsSet:
                while((i+count) in numsSet):
                    count += 1
                maxCount = max(count, maxCount)
                
        return maxCount
