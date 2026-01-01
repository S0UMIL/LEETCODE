class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]#making an empty list for stacks so that all the indexes can be stored here
        n=len(temperatures)
        answer=[0]*n
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:#this represents that if an new element comes from temperatures list which is bigger than the last number on the stack.
                prev_index=stack.pop()#pop the numbers in the stack. meaning it wont be used ever again
                answer[prev_index]=i-prev_index#calculating distance ie how long before we experienced an warmer day , updating this into an list defined before
            stack.append(i)#inserting the index in the stack variable so that the loops goes on for next numbers too
        return answer
