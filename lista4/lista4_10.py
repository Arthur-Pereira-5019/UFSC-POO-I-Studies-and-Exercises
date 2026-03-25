N =int(input())
i = 1
while(i <= N):
    X, Y = input().split()
    X = int(X)
    Y = int(Y)
    s = 0
    if(X != Y):
        ma = X
        me = Y
        if(Y > X):
            ma = Y
            me = X
        for j in range(me+1,ma):
            if(j % 2 == 1):
                s += j
    print(s)
    i += 1