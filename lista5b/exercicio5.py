v1 = ""
v2 = ""
v3 = ""
v4 = ""
v5 = ""
v6 = ""
v7 = ""
v8 = ""
v9 = ""
v10 = ""
v11 = ""
v12 = ""
v13 = ""
v14 = ""
v15 = ""
for i in range (1,16):
    M, N = input().split()
    if(i == 1):
        if(M > N):
            v1 = "A"
        else:
            v1 = "B"
    elif(i == 2):
        if(M > N):
            v2 = "C"
        else:
            v2 = "D"
    elif(i == 3):
        if(M > N):
            v3 = "E"
        else:
            v3 = "F"
    elif(i == 4):
        if(M > N):
            v4 = "G"
        else:
            v4 = "H"
    elif(i == 5):
        if(M > N):
            v5 = "I"
        else:
            v5 = "J"
    elif(i == 6):
        if(M > N):
            v6 = "K"
        else:
            v6 = "L"
    elif(i == 7):
        if(M > N):
            v7 = "M"
        else:
            v7 = "N"
    elif(i == 8):
        if(M > N):
            v8 = "O"
        else:
            v8 = "P"
    elif(i == 9):
        if(M > N):
            v9 = v1
        else:
            v9 = v2
    elif(i == 10):
        if(M > N):
            v10 = v3
        else:
            v10 = v4
    elif(i == 11):
        if(M > N):
            v11 = v5
        else:
            v11 = v6
    elif(i == 12):
        if(M > N):
            v12 = v7
        else:
            v12 = v8
    elif(i == 13):
        if(M > N):
            v13 = v9
        else:
            v13 = v10
    elif(i == 14):
        if(M > N):
            v14 = v11
        else:
            v14 = v12
    elif(i == 15):
        if(M > N):
            v15 = v13
        else:
            v15 = v14
print(v15)
    