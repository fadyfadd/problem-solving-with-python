def reverse_integer(nbr):
    value = 0

    while (nbr != 0):
        value = value * 10 + nbr % 10
        nbr = int(nbr/10)

    return value

print(reverse_integer(1000)) #1
print(reverse_integer(1)) #1
print(reverse_integer(125)) #521
print(reverse_integer(46120)) #2160
