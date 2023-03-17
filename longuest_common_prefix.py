class Solution:

    def longuest_common_prefix(self , strings):
        result = ""
        strings.sort(); 
        i = 0
        while (i<len(strings[0]) and i<len(strings[len(strings) - 1]) and strings[0][i] == strings[len(strings) - 1][i]):          
            result = result + strings[0][i:i+1]
            i=i+1

        return result 


print(Solution().longuest_common_prefix(["fadyfadd" , "fady faddoul" , "fady_faddoul@hotmail.com"])) #fady
print(Solution().longuest_common_prefix([""])) #
print(Solution().longuest_common_prefix(["fadyfadd"])) #fadyfadd
