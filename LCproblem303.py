class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix=[0]#making an new array where we are gonna store sum
        for num in nums:
            self.prefix.append(self.prefix[-1]+num)#-1 because we start from 0 ie [0,SumAt1,SumAt2]
        

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right+1]-self.prefix[left]#at last just return the values according to above system of numbers , right+1 bcuz we have predefined that prefix[0] = 0 therefore we use right+1
