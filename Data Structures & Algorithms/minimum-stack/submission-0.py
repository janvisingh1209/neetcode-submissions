class MinStack:

    def __init__(self):
        self.stack=[] # tracks all elements
        self.min_stack=[] # tracks min elements

        

    def push(self, x) -> None:
        self.stack.append(x)  #append element x
        if not self.min_stack or x<=self.min_stack[-1]:  #if min stack is empty or the current element is smaller than the previous one add it to stack
            self.min_stack.append(x)
        
        

    def pop(self) -> None:
        top=self.stack.pop()  #pops topmost element from stack
        if top==self.min_stack[-1]:  #pops if topmost element is also on top of min_stack
            self.min_stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]  #returns topmost element of stack 
        

    def getMin(self) -> int:
        return self.min_stack[-1]
        
