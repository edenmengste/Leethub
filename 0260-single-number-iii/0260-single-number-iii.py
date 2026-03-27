class Solution(object):
    def singleNumber(self, nums):
        count = Counter(nums)
        once = []
        for key in count:
            if count[key] == 1:
                once.append(key)
        return once
                
        