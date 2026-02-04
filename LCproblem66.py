class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        one=1
        i=0
        digits=digits[::-1]#reversing the string since all the operations are to be done on the ending of the array. (just making it convienent)
        while one:
            if i<len(digits):
                if digits[i]==9:#according to the question the number follows decimal system meaning adding 9+1 != 10 but == 1,0 in an array (important testcase)
                    digits[i]=0#making the last element 0 when 1 is being added to it 
                else:
                    digits[i]+=1#if not 9 normal case adding an number to the array
                    one=0#to end while loop
            else:
                digits.append(1)#now notice how a single number 9 became 2 different indexes 1,0 . this means we need to add space for this scenario simple concept of addition of carrying a number to another
                one=0
            i+=1#i should be iterating
        return digits[::-1]#finally reversing the string back to its original form with edited answer :D
      #outcome- couldnt solve this problem , couldnt think of a solution for this testcase. had to see solution and understand.
        
