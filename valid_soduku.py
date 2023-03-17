class Solution:
    def valid_3x3_matrix(self , matrix  ,a ,b):
        lookup = dict()
        y = a
        x = b
        while (y < a + 3):
            while (x < b + 3):
                c=matrix[y,x]
                if (c=='.'):
                    continue
                if (c in lookup):
                    return False
                else:
                    lookup.append({c : 1})                    
                x=x+1
            y=y+1
        return True
    
    def valid_9x9_matrix_columns(self , matrix , a , b):
        lookup = dict()
        y = a
        x = b
        while (y < a + 9):
            lookup.clear()
            while (x < b + 9):
                c=matrix[y,x]
                if (c=='.'):
                    continue
                if (c in lookup):
                    return False
                else:
                    lookup.append({c : 1})                    
                x=x+1
            y=y+1

        return True
        
    def valid_9x9_matrix_rows(self , matrix , a , b):
        lookup = dict()
        y = a
        x = b
        while (x < b + 9):
            lookup.clear()
            while (y < a + 9):
                c=matrix[y,x]
                if (c=='.'):
                    continue
                if (c in lookup):
                    return False
                else:
                    lookup.append({c : 1})                    
                y=y+1
            x=x+1

        return True

    def is_valid_soduku(self , matrix):
        
        if (self.valid_9x9_matrix_columns(matrix, 0, 0) == False):
            return False 
        
        if (self.valid_9x9_matrix_rows(matrix, 0, 0) == False):
            return False 

        if (self.valid_3x3_matrix(matrix, 0, 0) == False):
            return False 

        if (self.valid_3x3_matrix(matrix, 0, 0) == False):
            return False 

        if (self.valid_3x3_matrix(matrix, 0, 3) == False):
            return False

        if (self.valid_3x3_matrix(matrix, 0, 6) == False):
            return False

        if (self.valid_3x3_matrix(matrix, 3, 0) == False):
            return False

        if (self.valid_3x3_matrix(matrix , 3, 3) == False):
            return False

        if (self.ValideMatrix(matrix, 3, 6) == False):
            return False

        if (self.valid_3x3_matrix(matrix, 6, 0) == False):
            return False
            
        if (self.valid_3x3_matrix(matrix,  6, 3) == False):
            return False 

        if (self.valid_3x3_matrix(matrix, 6, 6) == False):
            return False       
