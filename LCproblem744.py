class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        right=len(letters)-1
        left=0
        while left<=right:
            mid=left+(right-left)//2
            mid_value=letters[mid]
            if mid_value<=target:#we want a character strictly greater than the target so we implement this
                left=mid+1
            else:# my doubt why dint we implement an == case like how we usally do. ans-Return the smallest letter strictly greater than target

                  #So for any letter:
                    #< target → ❌ invalid
                    #== target → ❌ invalid
                    #> target → ✅ valid
                    #There is no special meaning to equality here.

                right=mid-1
            
        return letters[left % len(letters)]#this is the part of code i dint understand / get . " What should i return? " for an specfic edge case like arr=[c,f,j] if target=j we have to return c 
                                          # for this purpose we use % why ? in the above case left=3 length=3 3%3==0 hence c will be returned

                
        
