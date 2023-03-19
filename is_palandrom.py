def is_palindrom(x):
    y = x
    value=0
    while (y != 0):
            value = value * 10 + (y % 10)
            y=int(y/10)
    return x==value

is_palindrom(121)
