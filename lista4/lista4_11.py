n =int(input())
i = 0
a0 = 0
a1 = 1
aa = 0
while(i < n):
    if(i == 0):
        print("0")
    elif(i == 1):
        print("1")
    else:
        aa = a1
        a1 = a1 + a0
        a0 = aa
        print(a1)
    i += 1