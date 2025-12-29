class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result=[]#create list to store continous sum
        cur_sum=0
        for num in range(0,len(nums)):
            cur_sum+= nums[num] #adding all the sums index by index and storing in an variable
            result.append(cur_sum)# add the data into the list and return it
        return result
