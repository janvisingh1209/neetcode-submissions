class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[] #tracks operands

        for token in tokens:
            if token not in '+-/*':
                stack.append(int(token))  #convert string token into int token
            else:
                b=stack.pop()   #topmost element becomes b and is popped
                a=stack.pop()    #2nd topmost element becomes a

                if token== '+': #operators are applied on a and b that were just popped 
                    stack.append(a+b)  #then pushed back onto stack
                elif token== '-':
                    stack.append(a-b)
                elif token== '*':
                    stack.append(a*b)
                elif token== '/':
                    stack.append (int(a/b))
        return stack[0]  #return the only element left in stack

            
                
                

        