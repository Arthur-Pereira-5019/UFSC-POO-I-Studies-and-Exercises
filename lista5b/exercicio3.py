while True:
    i = 0
    n = int(input())
    i =+ 1
    print("Teste {}".format(i))
    if (n==0):
        break
    s = 0
    for i in range (n):
        J, Z = input().split()
        J = int(J)
        Z = int(Z)
        s = s + J - Z
        print(s)
