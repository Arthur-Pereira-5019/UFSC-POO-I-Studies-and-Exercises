def verificaZ(x,z):
    if(z > x):
        return True
    else:
        return False

def ultrapassandoZ():
    x = int(input())
    while True:
        z = int(input())
        if(verificaZ(x,z)):
            break;
    s = x
    i = 0
    while (s < z):
        i += 1
        s = s + i
    print(i)

ultrapassandoZ()