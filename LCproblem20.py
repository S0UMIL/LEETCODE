#the problem talks about having closing and opening parenthesis in an valid order.
# (){}[]- valid , [{]}-not valid , ((((()))))-valid
#hence the logic here is to check for closing brackets first , cause if it starts with closing brackets its not valid
#then if we find a pair of valid parenthesis we pop it out of the stack.
#we keep repeating this process if the stack is empty in the end then we know its an valid parenthesis else not valid
class Solution:
    def isValid(self, s: str) -> bool:
      hashmap={
        ")":"(",
        "]":"[",
        "}":"{"
      }
      stack=[]
      for i in s:
        if i in hashmap:
          if stack and stack[-1]==hashmap[i]:
            stack.pop()
          else:
            return False
        else:
          stack.append(i)
      return True if not stack else False
            
          
