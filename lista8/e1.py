while True:
    n = int(input())
    if(n == 0):
        break
    c = input()
    d = -1*c.count("D")
    e = c.count("E")
    t = d+e
    r = t % 4
    if(r == 0):
        print("N")
    elif(r == 1):
        print("O")
    elif(r == 2):
        print("S")
    else:
        print("L")