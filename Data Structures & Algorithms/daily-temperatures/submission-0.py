class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        stack=[]  #stores indices
        res=[0]*n  
        for i,temp in enumerate(temperatures):
            while stack and temp>temperatures[stack[-1]]:
                prev_index=stack.pop()
                res[prev_index]=i-prev_index
            stack.append(i)
        return res