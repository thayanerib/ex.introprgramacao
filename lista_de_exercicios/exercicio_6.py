####Construa um programa que, tendo como dados de entrada dois pontos quaisquer no plano,
####P1(x1,y1) e P2(x2,y2), escreva a distância entre eles. A fórmula que efetua tal cálculo é:
import math
a = int(input("entre com um numero:"))
b = int(input(""))
c = int(input(""))
d = int(input(""))
dist = math.sqrt((c-a)**2 + (d-b)**2)
print(" A distancia entre P1,P2 é: %d " % dist)