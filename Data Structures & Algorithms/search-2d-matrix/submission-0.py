class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row=len(matrix)
        col=len(matrix[0])
        i=0
        j=row*col-1
        while i<=j:
            mid=(i+j)//2
            r=mid//col
            c=mid%col
            if matrix[r][c]==target:
                return True
            elif matrix[r][c]<target:
                i=mid+1
            else:
                j=mid-1
        return False


        