left=0
right=len(s)-1

while left < right:
    s[left],s[right] = s[right],s[left]#knew the logic just dint know the syntax to swap numbers
    left+=1
    right-=1
  #thoughtprocess- we have to reverse the string in the existing array so we simplely create 2 pointers one at the right end other at the left end.
  # then we just swap the pointers one by one in the loop and increase the left poisiton by one so tht is moves forward to next number and decrease the right position by one likewise.
