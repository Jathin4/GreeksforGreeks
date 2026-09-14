class Solution:
    def countZeroes(self, arr):
        # code here
        c = 0
        for i in range(len(arr)-1,-1,-1):
            if arr[i] == 0:
                c += 1
            elif arr[i] != 0:
                break
            
        return c
        