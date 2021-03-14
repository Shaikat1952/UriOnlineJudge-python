a,b,c,d=input().split(" ")
passs= ((float(a)*2+float(b)*3+float(c)*4+float(d)*1)/10)
if (passs>=7.0):
   print("Media: %.1f"%passs)
   print("Aluno aprovado.")
elif (passs<5.0):
    print("Media: %.1f"%passs)
    print("Aluno reprovado.")
elif(passs>=5.0 and passs<=6.9):
    x=float(input())
    tryagn=((x+passs)/2)
    print("Media: %.1f"%passs)
    print("Aluno em exame.")
    print("Nota do exame: %.1f"%x)
    if(tryagn>=5.0):
       print("Aluno aprovado.")
       print("Media final: %.1f"%tryagn)
    elif(tryagn<=4.9):
       print("Aluno reprovado.")
       print("Media final: %.1f"%tryagn)
    
