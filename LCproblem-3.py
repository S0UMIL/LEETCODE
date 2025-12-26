class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set=set()
        right=0#here we create a right pointer 
        left=0#and a left pointer
        max_len=0#variable to store the maximum length or output
        for right in range(len(s)):#right pointer is constraint till the end of string 
            while s[right] in char_set:# if a character is repeated the following actions take place
                char_set.remove(s[left])# the left pointer moves towards the right pointer , the entire left block is sort of eliminated now and is stored in the set 
                left += 1
            char_set.add(s[right])# if the character is not repeated it is simply added to the set
            max_len = max(max_len, right-left+1)# simple right-left is the distance or rather length of the characters and +1 is done to keep arrays indexes in-mind
        return max_len
#ps solved first medium level problem :D
