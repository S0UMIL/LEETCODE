class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new={}#creating a dictionary
        for i in strs:
            s = "".join(sorted(i))#first sorting the elements why? take case of "act" and "cat" if we sort this we get 2-act we can note this in the dictionary as its key:value
            if s not in new:
                new[s] = []
            new[s].append(i)#adding those sorted things into the dictionary
            
        return list(new.values())
