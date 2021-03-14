import math
n=input().split(" ")
n1=input().split(" ")
x1,y1=n
x2,y2=n1
rslt=float(x1-x2)
result=float(pow(rslt,rslt))
rslt1=float(y1-y2)
result1=float(pow(rslt1*rslt1))
sub=result-result1
sub1=float(math.sqrt(sub))
print("%.4f"%sub1)                                                            