###Escreva um programa que leia três números inteiros e positivos (A, B, C) e calcule a seguinte
##expressão:
#D=(R+S)/2, R=(A+B)**2 e S=(B+C)**2

A = int(input("Digite um número: "))
B = int(input("Digite um número: "))
C = int(input("Digite um número: "))
R = (A + B)**2
S = (B + C)**2
D = (R + S)/2
print(" O valor de D é: %d " % D)