n=input().split(" ")
a,b=n
x=int(a)
y=int(b)
if x==1:
    result=float(y*4.0)
    print("Total: R$ %.2f"%result)
elif x==2:
    result1=float(y*4.5)
    print("Total: R$ %.2f"%result1)
elif x==3:
    result2=float(y*5)
    print("Total: R$ %.2f"%result2)
elif x==4:
    result3=float(y*2)
    print("Total: R$ %.2f"%result3)
elif x==5:
    result4=float(y*1.50)
    print("Total: R$ %.2f"%result4)