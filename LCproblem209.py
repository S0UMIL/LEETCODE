class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        right=0
        left=0
        min_len=float('inf')#important line , dint check the constraints dude to which i kept getting runtime error
        
        a=0
        for right in range(len(nums)):
            a+=nums[right]
            while a>=target:#here we shrink the window till we get a=target because we want the min value for the size of subarray . for example target=7, [2,3,1,2,4,3] if right pointer goes till 5 and left is at 0 we keep shrinking until we reach atleast 7 or greater with minimum subarray size
                min_len=min(min_len,right-left+1)#in the above case mention the minimum would be 2, from subarray [4,3] , in this problem the whole catch was when do we shrink the window once that is done it was easy
                a-=nums[left]
                left+=1
            
            
        return 0 if min_len==float('inf') else min_len
