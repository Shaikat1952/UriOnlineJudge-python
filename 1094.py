from numpy import *
index=int(input)
a=zeros(index)
for x in range(index):
    numbr=int(input())
    a[x]=numbr
for x in range(index):
    print(a[x])