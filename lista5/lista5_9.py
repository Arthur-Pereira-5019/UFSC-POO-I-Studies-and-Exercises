i = 0
while True:
    i += 1
    n = int(input())
    if(n != 0):
        print("Teste {}".format(i))
        fA = 0
        fB = 0
        for i in range (n):
            A, B = input().split()
            A = int(A)
            B = int(B)
            fA += A
            fB += B
        if(fA > fB):
            print("Aldo")
        else:
            print("Beto")
    else:
        break
            