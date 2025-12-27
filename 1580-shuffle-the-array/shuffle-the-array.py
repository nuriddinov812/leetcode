class Solution(object):
    def shuffle(self, nums, n):
        result = []
        a=[]
        b=[]
        for i in range(len(nums)):
            if i < n:
                a.append(nums[i])
            else:
                b.append(nums[i])
        for i ,j in zip(a,b):
            result.append(i)  
            result.append(j)
        return result             

        