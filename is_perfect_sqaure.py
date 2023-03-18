def isPerfectSquare(num) -> bool:        
        value=1
        while (value*value < num):            
            value = value+1
        print (value*value)
        return value*value==num
isPerfectSquare(16)
    
