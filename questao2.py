def maior(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c
    return a

DViagem1 = 0
DViagem2 = 0
DViagem3 = 0
vendas1 = 0
vendas3 = 0
contVendedores1 = 0
Tservico = int(input())

while Tservico > 0:
    valorVendas = float(input())
    DViagem = float(input())

    if Tservico<5:
        DViagem1 +=DViagem
        vendas1 +=valorVendas
        contVendedores1 += 1
        # print(DViagem)
        
    elif Tservico>=5 and Tservico<=10:
        DViagem2+=DViagem


    elif Tservico>10:
        DViagem3 +=DViagem
        vendas3+= valorVendas

    Tservico = int(input())

maiorDviagem = maior(DViagem1, DViagem2, DViagem3)
if (maiorDviagem == DViagem1):
    print("Grupo 1")
elif (maiorDviagem == DViagem2):
    print("Grupo 2")
elif(maiorDviagem== DViagem3):
    print("Grupo 3")  

if contVendedores1 !=0:
    mediaVendasGrupo1 = vendas1 / contVendedores1   
else:
    mediaVendasGrupo1 = 0
valorLiquidoGrupo3 = vendas3 - DViagem3
Tviagem = DViagem1 + DViagem2 + DViagem3
        
print("%.2f" %mediaVendasGrupo1)
print("%.2f" %valorLiquidoGrupo3)
print("%.2f" %Tviagem)