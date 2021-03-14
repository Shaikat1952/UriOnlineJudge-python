x=float(input())
if(x>=0.00 and x<=2000.00):
    print("Isento")
elif(x>2000.00 and x<=3000.00):
    result=x-2000.00
    result=(result*8)/100
    print("R$ %.2f"%result)
elif(x>3000.00 and x<=4500.00):
    result=x-3000.00
    result=(result*18)/100
    result=result+80
    print("R$ %.2f"%result)
elif(x>4500.00):
    result=x-4500.00
    result=(result*28)/100
    result=result+80+270
    print("R$ %.2f"%result)