cadeia = input("string: ")
tamanho = len(cadeia)
palindromo = True
for i in range(tamanho//2):
    if cadeia [i]!= cadeia[tamanho-1-i]:
        palindromo = False
if palindromo:
    print("A palavra é palindromo")
else:
    print("A palavra não é palindromo")    


