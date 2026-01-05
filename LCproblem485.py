class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr_sum=0
        max_len=0#this is need to keep record of what was the maximum length
        for num in nums:
            if num==1:
                curr_sum+=1
                max_len=max(max_len,curr_sum)#the main ideology lies in this part of the code , if zero appear we want to skip it and carry on , so just keep updating max length before 0 appears then return .
            else:
                curr_sum=0# my fault was i only tried solving in one variable which i sooner realized wasnt making sense.
                
        return max_len
