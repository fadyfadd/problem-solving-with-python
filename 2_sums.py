def two_sums(nums , target):
    lookup=dict() 
    
    for i in range(0,len(nums)):
        delta = target - nums[i] 
        if (delta in lookup.keys()):
            return [lookup[delta] , i]
        else:
            lookup.update({nums[i] : i})      

print(two_sums([2,7,11,15] , 9)) #[0,1]

   