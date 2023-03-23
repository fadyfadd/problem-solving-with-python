def merge(nums1: list[int], m: int, nums2: list, n: int):
    
        i=0
        j=0
        res=[]
        
        while (i < m and j < n):
            if (nums1[i] < nums2[j]):
                res.append(nums1[i])
                i=i+1
            else:
                res.append(nums2[j])
                j=j+1
       
        while (i < m):
            res.append(nums1[i])
            i=i+1
        print(res)
        while (j < n):
            res.append(nums2[j])
            j=j+1

        for i in range(0,len(res)):
            nums1.insert(i , res[i])

        while (len(nums1) != m + n):
            nums1.pop(len(nums1) - 1)

print(merge([1,2,3,0,0,0],3 , [2,5,6] , 3)) #[1, 2, 2, 3, 5, 6]