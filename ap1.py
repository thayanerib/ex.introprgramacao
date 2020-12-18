quant = int(input())
cont = 0
quantPar = 0
quantImpar = 0
quantPrimo = 0
soma = 0
squadrado = 0


while cont<quant:

    numero = int(input())

    if cont == 0:
        maior = numero
        menor = numero

    if numero % 2 == 0:
        quantPar+=1
        print("Par",end=" ")
    else:
        quantImpar+=1
        print("Impar", end=" ")

    divisores = 0   

    for c in range (1,numero+1):
        if numero % c ==0:
            divisores +=1
    if divisores ==2: 
        quantPrimo+=1
        print("Primo", end=" ")

    quadrado = numero**2
    print("%d"%quadrado, end=" ")
    squadrado +=quadrado
    

    fat = 1
    for i in range(1,numero+1):
        fat*=i
    print(fat)
    soma+=numero

    if numero>maior:
        maior = numero
    if numero <menor:
        menor = numero    

    cont+=1
if quant>0:    
    mediaSoma = soma/quant
else:
    mediaSoma = 0.00
print(quantPar)
print(quantImpar)
print(quantPrimo)
print("%.2f" % mediaSoma)
print(squadrado)

if quant>0:
    print(maior)
    print(menor)







    
