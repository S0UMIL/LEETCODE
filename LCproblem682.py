class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[] #again an stack problem we create an empty set to store the data
        for o in operations:
            if o=="C":
                stack.pop()#beacuse the last element has to be removed
                
            elif o=="D":
                dd=stack[-1]*2#next element is double of previous
                stack.append(dd)
            elif o=="+":
                plus=stack[-1]+stack[-2] # next element is sum of previous 2 elements
                stack.append(plus)
            else:
                stack.append(int(o)) #if just int directly added to stack
        return sum(stack)
