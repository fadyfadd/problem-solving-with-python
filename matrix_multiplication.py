def multiply(matrix1 , matrix2) -> int:
        result = list()
        
        for i in range(0 , len(matrix1)):
            row=list()
            for j in range (0 , len(matrix2[0])):               
                cumule:int = 0
                for k in range(0,len(matrix2)):
                    cumule = cumule + matrix1[i][k] * matrix2[k][j]
                row.append(cumule)
            result.append(row)
        return result       

print(multiply([[1,2,3,8]],[[1,2],[1,2],[1,2],[1,2]]))  #[14,28]

           