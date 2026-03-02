n=int(input())
if n>=0  and n<10:
    print(n**2)
elif n>=10 and n<100:
    import math
    p=math.sqrt(n)
    print(p)
elif n>=100 and n<1000:
    print(n**(1/3))
else:
    print("invalid")