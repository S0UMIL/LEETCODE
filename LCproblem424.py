right=0#declaring right pointer and left pointer
left=0
max_len=0#this will store the max length of substring
max_freq=0#this will store the max frequency of a particular character
freq={}#hashmap
for right in range(len(s)):
    freq[s[right]]= freq.get(s[right],0) + 1#if we notice a character we simply add its frequency into the hashmap.
    max_freq=max(max_freq,freq([s[right]]))#updating the maxmimum frequency out of all characters
    if (right-left+1) - max_freq >k:#this conditon is to shrink the window size.
        freq[s[left]]-=1
        left+=1
    max_len=max(max_len,right-left+1)
return max_len
#Mistake1- i kept initialzing the if statement first for left pointer rather than the right pointer this was wrong bcuz if we do this max_freq wont be updated meaning our logic for line9 wont make any sense
#Mistake2- faced alot of syntax errors in line 8 and 7 with brackets n stuff . NOW RESOLVED
