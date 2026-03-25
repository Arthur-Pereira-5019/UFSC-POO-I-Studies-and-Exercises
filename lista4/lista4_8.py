while True:
    N, M = input().split()
    N = int(N)
    M = int(M)
    if(N == 0 or M == 0):
        break
    else:
        
        r = ""
        s = 0
        i = N
        m = M
        if(N > M):
            i = M
            m = N
        
        while(i < m):
            r = r + str(i) + " "
            s += i
            i += 1
        s += m
        print(r + str(m) + " Sum="+str(s))


