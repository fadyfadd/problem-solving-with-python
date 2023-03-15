class solution:

    def isValid(self , s:str):
        
        if (len(s)==0):
            return True

        if (len(s)<2):
            return False; 
        
        brackets = {"{" : "}" , "[" : "]" , "(" : ")"}        
     
        stk = []

        for i in range(0,len(s)):
            br = s[i:i+1]

            if (br in brackets):
                stk.append(br)
            else:
                
                if (len(stk)==0): 
                    return False; 
                
                value = stk.pop()   
                u=brackets[value]                
                if (brackets[value] != br):
                    return False; 

        return len(stk)==0; 


print(solution().isValid("{}")) #True
print(solution().isValid("{[()()]}")) #True
print(solution().isValid("{")) #False
print(solution().isValid("")) #True
print(solution().isValid("{[()()]")) #False
print(solution().isValid("{[())]")) #False

 