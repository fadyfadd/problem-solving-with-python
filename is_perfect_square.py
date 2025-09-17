def is_perfect_square(num) -> bool:        
        
    if num < 0:
        return False  
    if num <= 1:       
        return True 
    value=1
    while (value*value < num):            
        value = value+1
    print (value*value)
    return value*value==num

print(is_perfect_square(16))
    
