def reverse_string(s: list):
        i=0
        j=len(s) - 1

        while (i<j):
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
            i=i+1
            j=j-1
        return None

a=[1,2,2,3]
reverse_string(a)
print(a) #[3,2,2,1]