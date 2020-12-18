def primo(n):
    divisores = 0
    for i in range (1,n+1):
        if n % i ==0:
            divisores +=1
    if divisores ==2: 
        return True 
    else:
        return False 
n = int(input("Quantos primos: "))
i = 2
j = 0
while True:
    if primo(i):
        print(i, end=" ")
        j = j +1
    i = i +1
    if j == n:
        break

        
        


