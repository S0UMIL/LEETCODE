class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       new={}#creating a hashmap
        for i in strs:
            s="".join(sorted(i))#suppose a word like eat, it is sorted into a,e,t= aet and this sorting converts it into list in this form - [a,e,t] to join the whole into one word we do "".join
            if s not in new:#if a aet not in hashmap then
                new[s]=[]#create a new key simple
            new[s].append(i)#if key already exists add it in form of list for ex- aet(key)=[ate] now comes a word tae which is also an anagram of aet so it is just appended into the list and becomes [ate,tae]
        return list(new.values())#we have to return an list as asked in the question so list(..)
