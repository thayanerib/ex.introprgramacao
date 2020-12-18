import math
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
delta = b**2 - 4*a*c
if delta < 0:
    print(" Não existem raizes reias.")
else:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print("x1 = %6.2f, x2 = %6.2f" % (x1,x2))