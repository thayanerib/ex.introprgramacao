Quantidade = int(input("Quantas notas?"))
quant1 = 1
acumuladora = 0

while quant1<=Quantidade:
    quant1 +=1
    nota = float(input("nota:"))
    acumuladora += nota
SomaNota = acumuladora/Quantidade
print("Média:%3.2f"%SomaNota)    