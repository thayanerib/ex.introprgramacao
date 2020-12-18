anos = int(input("Quantos anos você tem?:"))
meses = int(input("Quantos meses você tem?:"))
dias = int(input("Quantos dias você tem?:"))
A = anos*365
M = meses*30
D = dias+A+M
print("você tem %d dias de vida" % D)