#O custo ao consumidor de um carro novo é a soma do custo de fábrica com a percentagem do
#distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que a percentagem do
#distribuidor seja de 28% e os impostos de 45%, escrever um programa que leia o custo de fábrica de
#um carro e escreva o custo ao consumidor.

fabrica = float(input("Custo de fabrica: ")
vimposto = float(input(""))
vdistribuidor = float (input(""))
imposto = fabrica + (fabrica*vimposto/100)
distribuidor = fabrica+(fabrica*vdistribuidor/100)
consumidor = fabrica + distribuidor + imposto
print(" R$ %6.2f" % consumidor)

