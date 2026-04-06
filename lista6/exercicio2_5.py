def verifica_entrada(x,l):
    if(not (1 <= x <= l)):
       print("Valor inválido, digite novamente!")
    return x

def colchao(a,b,c,h,l):
    melp = min(h,l)
    malp = max(h,l)
    melc = min(a,b,c)
    malc = max(a,b,c)
    smelc = 0
    if(malc == a):
        smelc = max(b,c)
    elif(malc == b):
        smelc = max(a,c)
    else:
        smelc = max(a,b)
    if(melc <= melp and smelc <= malp):
        print("S")
    else:
        print("N")
        
a = 0
b = 0
c = 0
h = 0
l = 0
while True:
    a,b,c = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    if(verifica_entrada(a,300) and verifica_entrada(b,300) and verifica_entrada(a,300)):
        break
while True:
    h,l = input().split()
    h = int(h)
    l = int(l)
    if(verifica_entrada(h,250) and verifica_entrada(l,250)):
        break
    
    
colchao(a,b,c,h,l)

