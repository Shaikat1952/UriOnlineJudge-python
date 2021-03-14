a,b,c,d=list(map(int,input().split()))
if(a==c and b==d):
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
elif(a<c and b<d):
    a=c-a
    b=d-b
    print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(a,b))
elif(a<c and b>d):
    b=d+60-b
    a=(c-1)-a
    print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(a,b))

