def miliseconds(h,m,s):
    h = h * 3600
    m = m * 60
    s = s
    miliseconds = h + m + s
    return '{} Miliseconds'.format(miliseconds)


h,m,s = [int(x) for x in input().split()]
print(miliseconds(h,m,s))