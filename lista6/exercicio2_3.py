def verifica_entrada(x):
    if(x > 1000 or x < 1):
        return False
    else:
        return True

def verifica_entrada_zero(x):
    if(x > 1000 or x < 0):
        return False
    else:
        return True

def controle_capacidade():
    N = 0
    C = 0
    while True:
        N,C = input().split()
        N = int(N)
        C = int(C)
        if(verifica_entrada(N) and verifica_entrada(C)):
            break
    tp = 0
    i = 0
    excedeu = False
    while True:
        if (i == N):
            break
        S,E = input().split()
        S = int(S)
        E = int(E)
        if(not verifica_entrada_zero(S) or not verifica_entrada_zero(E)):
            continue
        tp = tp+E-S
        if(tp > C):
            excedeu = True
        i += 1
    if(excedeu):
        print("S")
    else:
        print("N")

controle_capacidade()
        
    