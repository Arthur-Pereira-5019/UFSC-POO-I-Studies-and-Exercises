def verifica(x):
    while(x < 2 and x > 300):
        x = int(input("Valor inválido, digite um valor entre 0 e 1"))
    return x

def eprimo(x):
    for i in range (2,x-1):
        if(x % i == 0):
            return False
    return True

primos = 0
for i in range (10):
    n = int(input())
    n = verifica(n)
    if(eprimo(n)):
        primos +=1
print(primos)
    
    
