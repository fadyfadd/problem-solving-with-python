def to_2_base(n:int):
        lst=list()
        if (n==0):
            lst.append(0)            
            return lst
        
        while (n!=0):
            lst.append(n%2)
            n=int(n/2)
        lst.reverse()       
        return lst

def countBits(n: int):
        res=list()
        for i in range(0,n+1):
            lst=to_2_base(i)
            k=list(filter(lambda x : x==1,lst))
            res.append(len(k))
        return res


print(countBits(5)) #[0, 1, 1, 2, 1, 2]
print(countBits(0)) #[0]
print(countBits(1)) #[0,1]