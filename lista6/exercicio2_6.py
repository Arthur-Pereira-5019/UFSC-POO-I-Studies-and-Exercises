pares = 0
impares = 0
def verifique(n):
    if(n % 2 == 0):
        return "Par"
    else:
        return "Impar"
for i in range (10):
    v = int(input("Digite um valor: "))
    if(verifique(v) == "Par"):
        pares += 1
    else:
        impares += 1
        
print("Foram digitados no total {} pares e {} ímpares".format(pares,impares))
    