class Solution:

    def encode(self, strs: List[str]) -> str:
        elements = ""#creating an empty string 
        for i in range(len(strs)):
            elements += str(len(strs[i])) + "#" + strs[i]#from the starting to ending of list adding all elements , seperated by #
        return elements

    def decode(self, s: str) -> List[str]:
        strs = []#empty list
        i = 0
        while i < len(s):
            j = s.find("#", i)# here'#' acts as a index seperator in the string itself meaning wherever # is present an new index starts
            length = int(s[i:j])
            strs.append(s[j+1 : j+1+length])#adding all the string characters into the list
            i = j + 1 + length#updating the length to end loop
        return strs
