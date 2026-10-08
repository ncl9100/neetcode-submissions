class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #find row
        left = 0
        right = len(matrix) - 1
        while left <=right:
            row_mid = (left + right)//2
            if matrix[row_mid][0] > target and matrix[row_mid][len(matrix[0])-1] > target:
                right = row_mid -1
            elif matrix[row_mid][0] < target and matrix[row_mid][len(matrix[0])-1] < target:
                left = row_mid + 1
            else:
                #start finding columns now
                found_row = row_mid
                left = 0
                right = len(matrix[0])-1
                while left<=right :
                        column_mid = (left + right)//2
                        if matrix[row_mid][column_mid] < target:
                            left = column_mid + 1
                        elif matrix[row_mid][column_mid] > target:
                            right = column_mid - 1
                        elif matrix[row_mid][column_mid] == target:
                            return True
                        else:
                            return False
        return False


        
        