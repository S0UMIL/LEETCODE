class Solution:
    def twoSum(self, nums, target):
        new=[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j:
                    if nums[i]+nums[j]==target:
                        new.append(i)
                        new.append(j)
                        return new
