n=int(input())
if n>=0 and n<10:
	print(n**2,end="\n")
elif n>=10 and n<100:
	print(f"{n**(1/2):.2f}",end="\n")
elif n>=100 and n<1000:
	print(f"{n**(1/3):.2f}",end="\n")
else:
	print("Invalid",end="\n")
