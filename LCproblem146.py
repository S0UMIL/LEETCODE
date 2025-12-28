left=0
right=len(numbers)-1 # classic 2 pointer problem

while left < right: # left pointer represents the smaller numbers towards the left end and the right pointer represents the bigger numbers towards the right end , this is possible since the array is already sorted
    current_sum= numbers[left] + numbers[right] # storing sum value
    
    if current_sum==target:
        return [left+1,right+1] # important to remember to always do +1 to remove it from index form.


    elif current_sum<target:#if sum < target we simply move the left pointer towards theright handside.
        left+=1
    else:
        right-=1# if sum > target we move right pointer towards left handside.
    
