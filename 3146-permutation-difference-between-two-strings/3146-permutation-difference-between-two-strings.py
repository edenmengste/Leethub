class Solution(object):
    def findPermutationDifference(self, s, t):
        res = 0
        for i, char_s in enumerate(s):
            for j, char_t in enumerate(t):
                if char_s == char_t:
                    res += abs(i-j)
                    break
        return res            
        