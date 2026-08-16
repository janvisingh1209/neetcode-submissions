class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #think of it as a 1d matrix 
        m=len(matrix)#rows
        n=len(matrix[0]) #cols
        start=0
        end=m*n-1
        while start<=end:
            mid=(start+end)//2
            row=mid//n
            col=mid%n
            mid_val=matrix[row][col]
            if mid_val<target:
                start=mid+1
            elif mid_val==target:
                return True
    
            else:
                end=mid-1

        return False
        #time complexity: o(log(mn))




        