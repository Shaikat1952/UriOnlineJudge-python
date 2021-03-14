dia1,num1=input().split(" ")
num1=int(num1)
hora1,minuto1,segendo1=input().split(":")
hora1=int(hora1);minuto1=int(minuto1);segendo1=int(segendo1)
dia2,num2=input().split(" ")
num2=int(num2)
hora2,minuto2,segendo2=input().split(":")
hora2=int(hora2);minuto2=int(minuto2);segendo2=int(segendo2)

second1=(segendo1+hora1*60*60+minuto1*60+num1*24*60*60)
second2=(segendo2+hora2*60*60+minuto2*60+num2*24*60*60)
finalSec=second2-second1
day=finalSec//24*60*60
hours = (finalSec-day*24*60*60)//3600
min=(finalSec-day*24*60*60-hours*3600)//60
second=(finalSec-day*24*60*60-hours*3600-min*60)
print("{} dia(s)".format(day))
print("{} hora(s)".format(hours))
print("{} minuto(s)".format(min))
print("{} segundo(s)".format(second))
