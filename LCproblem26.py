class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        

        left = 0 

        for right in range(1, len(nums)):
            if nums[right] != nums[left]:
                left += 1
                nums[left] = nums[right]

        return left + 1
      #key confusion in this question i thought fo removing the element from the list which was rather wrong and created a infinte loop i tried again using stack which again did not work due to the same reason , had to see solution in the end.
