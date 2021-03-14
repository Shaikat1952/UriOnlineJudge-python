x=int(input())
years=int(x/356)
temp=int(x%365)
month=int(temp/30)
days=temp%30
print("%d ano(s)"%years)
print("%d mes(es)"%month)
print("%d dia(s)"%days)