class solution:

    def printFibonacci(self , nbr:int):
        a_1:int
        a_2:int
        a_1 = 0
        a_2 = 1
        sum:int = a_1 + a_2
        for i in range(0,nbr):
            print(sum)
            a_1 = a_2 
            a_2 = sum
            sum = a_1 + a_2

solution().printFibonacci(10)

            
        
