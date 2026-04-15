def calcular(n):
    if(len(n) == 1):
        if(n == "3" or n == "6" or n == "9"):
            return "Sim"
        return "Não"
    else:
        nn = 0
        for i in range(len(n)):
            nn += int(n[i])
        return calcular(str(nn))
    
while True:
    a,b = input().split()
    print(calcular(b))
    c = input("Deseja continuar? ")
    if c == "N":
        break
print("Fim")