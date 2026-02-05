#learnt binary search , solving binary search related problems

#2nd submission (corrected answer)
class Solution:
    def firstBadVersion(self, n: int) -> int:
      right=n
      left=1
      while left<=right:
        mid=left + (right-left) //2
        a=isBadversion(mid)
        if a==True:
          left=mid+1
        elif a==False:
          right=mid-1
      return left


#first submission (wrong answer 9/24 testcases)
class Solution:
    def firstBadVersion(self, n: int) -> int:
      right=n
      left=1
      while left<=right:
        a=isBadversion(version)#dint understand how to use the API , thought that all the binary search related material is present in this fn including mid etc which i was wrong abt.
        if a==True:
          return n # shld not immediately return after true shouldve moved right pointer back to confirm it then move on , failed to implement the binary logic 
    
