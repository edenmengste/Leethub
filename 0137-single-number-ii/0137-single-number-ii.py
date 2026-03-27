class Solution(object):
    def singleNumber(self, nums):
        counts = Counter(nums)
        for Key in counts:
            if counts[Key] < 3:
              return Key
        