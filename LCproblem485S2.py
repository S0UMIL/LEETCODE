class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
            curr_sum=0
            nsum=0
            for i in range(len(nums)):
                if nums[i]==1:
                    curr_sum+=1
                    nsum=max(curr_sum,nsum)#imp here kept using max() which is not iterable had to give range
                elif nums[i]==0:
                    curr_sum=0
            return nsum
        
        
            

        
