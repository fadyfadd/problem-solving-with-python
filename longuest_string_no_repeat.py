def longuest_string_no_repeat(item):
    lookup=dict()
    start = 0
    end = 0
    count = 0
    max_count = 0

    while (end < len(item)):
        c=item[end:end+1]
        if (c not in lookup):
            count=count+1
            lookup.update({c:end})
            end=end+1
        else:
            max_count = max(max_count , count)            
            start = lookup[c] + 1
            end = lookup[c] + 1
            count = 0
            lookup.clear()
    max_count = max(max_count , count)
    return max_count
    

print(longuest_string_no_repeat("fadyfaddoul")) #4
print(longuest_string_no_repeat('')) #0
print(longuest_string_no_repeat('aa')) #1
print(longuest_string_no_repeat("abcddefghijk")) #8