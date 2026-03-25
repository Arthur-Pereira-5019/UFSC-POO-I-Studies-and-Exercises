while True:
    v = int(input())
    if(v == 0):
        break
    else:
        i = 1
        r = ""
        while(i < v):
            r = r + str(i) + " "
            i += 1
        print(r + str(v))

