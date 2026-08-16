class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        bracket_map={')':'(',']':'[','}':'{'}

        for char in s:
            if char in bracket_map.values():
                stack.append(char)
            elif char in bracket_map:
                if not stack or stack[-1]!=bracket_map[char]: #if stack is empty or top element doesnt match the closing char in map
                    return False 
                else:
                    stack.pop()
            else:
                return False #invalid character

        return len(stack)==0