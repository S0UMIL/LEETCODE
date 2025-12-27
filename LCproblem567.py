class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        freq1={}
        freq2={}
        right=0
        left=0
        for i in range(len(s1)):#we will create an window based on the size of s1
            freq1[s1[i]]= freq1.get(s1[i],0) + 1#adding character frequencies in respective dictionaries
            freq2[s2[i]]= freq2.get(s2[i],0) + 1
        if freq1==freq2:
            return True
        for right in range(len(s1),len(s2)):#now right pointer checking for similar characters and frequencies
            freq2[s2[right]]=freq2.get(s2[right],0) + 1 # a new character added to window
            freq2[s2[left]]-=1 # removing the left most character
            if freq2[s2[left]]==0:#important condition i did not keep track of. in this we simply say after removing the left most element if the frequency becomes 0 we just remove it from the hashmap it self.
                del freq2[s2[left]]
            left +=1# moving the left pointer towards the right
            if freq1==freq2:
                return True
        return False
