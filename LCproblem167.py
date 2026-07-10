class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      i=0
      j=len(nums)-1
      new=[]
      while i>j:
        if nums[i]+nums[j]==target:#this here is very similar to binary search algo 
          if i!=j:#because given in the question that 2 indexs have to be different
            new.append(i)
            new.append(j)
            return new
            break
        elif nums[i]+nums[j]>target:
          j-=1
        else:
          i+=1
        
