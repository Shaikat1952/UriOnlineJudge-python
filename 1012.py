x=input().split(" ")
a,b,c=x
TRIANGULO=(float(a)*float(c))/2
CIRCULO= 3.14159*float(c)*float(c)
TRAPEZIO=(float(a)+float(b))/2
TRAPEZIO1=TRAPEZIO*float(c)
QUADRADO=float(b)*float(b)
RETANGULO=float(a)*float(b)
print("TRIANGULO: %.3f"%TRIANGULO)
print("CIRCULO: %.3f"%CIRCULO)
print("TRAPEZIO: %.3f"%TRAPEZIO1)
print("QUADRADO: %.3f"%QUADRADO)
print("RETANGULO: %.3f"%RETANGULO)
