right=0
left=0
zerocount=0
max_len=0
for right in range(len(nums)):
  if nums[right]==0:
    zerocount+=1
  while zerocount>k:
    if nums[left]==0:#in this specifc part of code i had a error the error was i was running left+=1 basically moving the pointer first then updating the  zeros which was wrong and the problem
      zerocount-=1
    left+=1
  max_len=max(max_len,right-left+1)
return max_len
#this problem doesnt require any set or hashmap that was one part which kept me confused so new learning .
