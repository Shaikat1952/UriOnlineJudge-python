n=input().split(" ")
a,b,c=n
if int(a)>int(b) and int(a)>int(c):
    print("{} eh o maior".format(a))
elif int(a)<int(b) and int(c)<int(b):
    print("{} eh o maior".format(b))
elif int(a)<int(c) and int(b)<int(c):
    print("{} eh o maior".format(c))