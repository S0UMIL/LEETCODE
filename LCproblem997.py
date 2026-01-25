#1st submission
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        square=[]
        for right in range(len(nums)):
            sq=nums[right]**2# simple just created another list in which im storing all the square values then im sorting the list.
            square.append(sq)

            sort_nums=sorted(square)
        return sort_nums
      #not the most optimal solu will try it again
