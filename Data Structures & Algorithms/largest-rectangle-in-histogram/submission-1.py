class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        left=[-1]*n
        right=[n]*n
        stack=[]
        #find left value:
        for i in range(len(heights)):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            if stack:  #without this index error
                left[i]=stack[-1]
            stack.append(i)
        stack.clear()
           #find right value
        for i in range(n-1,-1,-1):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            if stack:
                right[i]=stack[-1]
            stack.append(i)
    # calculate max area
        max_area=0
        for i in range(len(heights)):
            height=heights[i]
            width=right[i]-left[i]-1
            max_area=max(max_area,height*width)
        return max_area
# time complexity=o(N)

            
        