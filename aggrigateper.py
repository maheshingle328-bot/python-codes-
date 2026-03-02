def agri_per(n,marks):
    agripercent=(sum(marks)/(n*100))*100
    return agripercent
n=int(input("Total no of cources:"))
marks=[]
for i in range(n):
    
    score=int(input())
    if score<40:
        print("fail")
    else:
        marks.append(score)
agripercent=agri_per(n,marks)        
print(agripercent)
if agripercent>75:
    print("grade A")
elif agripercent<75 and agripercent>=50:
    print("grade B")
else:
    print("grade C")