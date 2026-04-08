def soma(x,y):
    s = 0
    for i in range(x,y+1):
        s += i
    return s

def subtracao(x,y):
    a = min(x,y)
    b = max(x,y)
    return b-a

while True:
    x, y = input("Digite o intervalo: ").split()
    x = int(x)
    y = int(y)
    s = soma(x,y)
    print("Soma do intervalo = {}".format(s))
    
    x, y = input("Digite 2 valores: ").split()
    x = int(x)
    y = int(y)
    s = subtracao(x,y)
    print("Diferença = {}".format(s))

    if(input("Deseja continuar? ") != "S"):
        break

        