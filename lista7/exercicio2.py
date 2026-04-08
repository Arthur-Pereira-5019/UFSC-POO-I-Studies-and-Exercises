def verifica(x,en):
    if(en):
        while(x <= 0):
            x = int(input("Valor inválido, digite um valor positivo: "))
    else:
        while(x < 10 or x > 100):
            x = int(input("Valor inválido, digite um valor entre 10 e 100: "))
    return x

def inicio():
    n = int(input("Digite a quantidade de pipas: "))
    verifica(n,True)
    for i in range (n):
        x, y = input("Digite x e y ").split()
        x = int(x)
        x = verifica(x,False)
        y = int(y)
        y = verifica(y,False)
        print("Área: {} cm2".format((x*y)/2))

inicio()