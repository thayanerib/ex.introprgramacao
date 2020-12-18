QuantNumeros = int(input("Quantos números?"))
c = 0
maior = 0

while c<=QuantNumeros :
    c+=1
    numero = int(input("Informe o número: ")) 
    if numero>maior:
        maior = numero
print(" maior valor é : %s" %maior)