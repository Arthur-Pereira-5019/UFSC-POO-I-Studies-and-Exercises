def verifica(x,en):
    if(en):
        while(x <= 0):
            x = int(input("Valor inválido, digite um valor positivo: "))
    else:
        while(x < 2 or x > 100):
            x = int(input("Valor inválido, digite um valor entre 2 e 100: "))
    return x

def maiorPrimo(x):
    maiorprimo = 2
    for i in range(x+1):
        primo = 0
        if(eprimo(i)):
            primo = i
        if(primo > maiorprimo):
            maiorprimo = primo
    return maiorprimo

def eprimo(x):
    for i in range (2,x-1):
        if(x % i == 0):
            return False
    return True

n = int(input("Número de verificações: "))
n = verifica(n,True)
for i in range (n):
    N,M = input("Digite os valores de N e M: ").split()
    N = int(N)
    verifica(N,False)
    M = int(M)
    verifica(M,False)
    P1 = maiorPrimo(N)
    P2 = maiorPrimo(M)
    print(P1*P2)
print("Fim")
    
    

