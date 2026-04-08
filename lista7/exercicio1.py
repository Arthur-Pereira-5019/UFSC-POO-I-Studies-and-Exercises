def verifica(x):
    while(x != 0 and x != 1):
        x = int(input("Valor inválido, digite um valor entre 0 e 1"))
    return x

def ganhador(A,B,C):
    if(A == B == C):
        if(A == 0):
            return False
        else:
            print("*")
            return True
    if(A != B and A != C):
        print("A")
    elif(B != A and B != C):
        print("B")
    else:
        print("C")
    return True
def jogo():
    while True:
        A = 0
        B = 0
        C = 0
        A = int(input())
        A = verifica(A)
        B = int(input())
        B = verifica(B)
        C = int(input())
        C = verifica(C)
        if not ganhador(A,B,C):
            break
jogo()
        