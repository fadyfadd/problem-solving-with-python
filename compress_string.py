def compress(phrase):
    last_char = ''
    last_count = 0
    result = ''

    if (phrase == ''):
        return ''
    
    for c in phrase:
        if (c!=last_char):
            if (last_count > 1):               
                result = result +  last_char  + str(last_count)                 
            else:                
                result = result + last_char
            last_count = 1
            last_char = c               
        else:
            last_count = last_count + 1
         
    if (last_count == 1):
        result = result + last_char
    else:
         result = result + last_char + str(last_count)

    return result

print(compress('fady')) #fady
print(compress('')) #
print(compress('fady faddoul')) #fady fad2oul
print(compress('Rockwell')) #Rockwel2
print(compress('     ')) # 5
print(compress('x     xz')) #x 5xz