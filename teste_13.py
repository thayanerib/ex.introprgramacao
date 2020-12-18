def fatorial(n):
    fat = 1 
    for i in range(1,n+1):
       fat *= i
    return fat
FatNumero = fatorial(7)
print("Fatorial: %d" %FatNumero)   