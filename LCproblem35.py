class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #the array is sorted in ascending order, we need to insert an element inb/w any two elements
        right=len(nums)-1
        left=0
        while left <= right:
            mid=left+(right-left)//2
            mid_value=nums[mid]
            if mid_value==target:
                return mid
            elif mid_value<target:
                left=mid+1
            elif mid_value>target:
                right=mid-1
        return left
      #easy porblem solved using binary search algorithm.
