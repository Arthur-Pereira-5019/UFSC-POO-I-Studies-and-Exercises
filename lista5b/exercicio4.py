while True:
    i = 0
    n = int(input())
    i =+ 1
    print("Teste {}".format(i))
    if (n==0):
        break
    else:
        H = n//50
        n = n - H*50
        
        I = n//10
        n = n - I*10
        J = n//5
        n = n - J*5
        K = n
        print("{} {} {} {}".format(H,I,J,K))