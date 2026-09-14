class Solution:
    def countZeroes(self, arr):
        # code here
        c = 0
        for i in arr:
            if i == 0:
                c += 1
        return c