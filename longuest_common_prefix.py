def longuest_common_prefix(strings):
        result = ""
        strings.sort(); 
        i = 0
        while (i<len(strings[0]) and i<len(strings[len(strings) - 1]) and strings[0][i] == strings[len(strings) - 1][i]):          
            result = result + strings[0][i:i+1]
            i=i+1

        return result 

print(longuest_common_prefix(["fadyfadd" , "fady faddoul" , "fady_faddoul@hotmail.com"])) #fady
print(longuest_common_prefix([""])) #
print(longuest_common_prefix(["fadyfadd"])) #fadyfadd
