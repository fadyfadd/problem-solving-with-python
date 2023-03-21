def find_all_permutations(nums):
     if (len(nums)==1):
        return [[nums[0]]]
     
     data=[]

     for i in range(0 , len(nums)):
         
         item=nums[i]
         nums_1 = nums[:]
         nums_1.pop(i)
         res=find_all_permutations(nums_1)
         for a in res:
                a.insert(0,item)
                data.append(a)                  

     return data; 
             

print(find_all_permutations([1,2,3])) #[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
print(find_all_permutations([1,2])) #[[1, 2], [2, 1]]