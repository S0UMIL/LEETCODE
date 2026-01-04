class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        
        left = 0
        window_mul = 1#cant keep 0 otherwise whole multiplication wuld result in 0
        count = 0

        for right in range(len(nums)):
            window_mul *= nums[right]#multiplying all numbers in the array

            while window_mul >= k:#if this condition we met we just divide the numbers we multipled to remove the left side numbers
                window_mul //= nums[left]
                left += 1

            count += right - left + 1

        return count
