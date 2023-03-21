def check_if_contains_duplicates(nums):
    lookup=dict()

    for entry in nums:
        if (entry in lookup.keys()):
            return True
        else:
            lookup.update({entry:1})
    return False
        
print(check_if_contains_duplicates([1,1,1,3,3,4,3,2,4,2])) #True
print(check_if_contains_duplicates([])) #False
print(check_if_contains_duplicates([1,2,3,4,5])) #False