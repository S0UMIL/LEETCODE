class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left=0
        value_sum=0
        max_sum=float('-inf')
        for right in range(len(nums)):
            value_sum+=nums[right]
            if right-left+1==k:
                max_sum=max(max_sum , value_sum)
                value_sum-=nums[left]
                left+=1
        return max_sum/k
        
