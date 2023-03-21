def is_perfect_square(num) -> bool:        
        value=1
        while (value*value < num):            
            value = value+1
        print (value*value)
        return value*value==num
is_perfect_square(16)
    
