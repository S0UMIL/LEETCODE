class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count=0
        
        newL=[]#making a new list to store updated values of list
        
        while val in nums:
            nums.remove(val)
            
            newL=nums#replacing old list with new list so that changes are saved out of loop
        print(newL)
