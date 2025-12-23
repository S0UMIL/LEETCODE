class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res= "" #making a result variable to easily return values later on
        for i in range(len(strs[0])):# looping through the entire set of characters of the first string
            for s in strs:#going through every single string now 
                if i==len(s) or s[i] != strs[0][i]: #in the second condition we keep continuing the loop as long as the string is same with the str index string , if anything different loop breaks. meaning if any different character comes across the 2 string the loop breaks. a simple example can be 2 words flower and flight , the loop continues for the first 2 letters then breaks due to the difference in the letters o and i resepctively
                    return res # simply return blank if nothing is matching
            res += strs[0][i] # adding the specifc prefix to the result variable
        return res
