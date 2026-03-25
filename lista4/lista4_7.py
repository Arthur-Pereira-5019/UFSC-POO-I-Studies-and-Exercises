a = 0
g = 0
d = 0
while True:
    v = int(input())
    if(v == 4):
        break
    elif(v < 4):
        if(v == 1):
            a += 1
        elif(v == 2):
            g += 1
        else:
            d += 1

print("MUITO OBRIGADO")
print("Alcool: {}".format(a))
print("Gasolina: {}".format(g))
print("Diesel: {}".format(d))



