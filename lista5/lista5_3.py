X = int(input())
Z = 0
while (True):
    Z = int(input())
    if(Z > X):
        break
i = 0
a = 0
while (a < Z):
    a += X+i
    i += 1
print(i)
    