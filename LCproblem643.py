class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        window_sum = 0
        max_sum = float('-inf')#need answer with error less than 10^-5 

        for right in range(len(nums)):
            window_sum += nums[right]#adding all the elements into window

            if right - left + 1 == k:
                max_sum = max(max_sum, window_sum)
                window_sum -= nums[left]
                left += 1
        return max_sum/k
        
