n = int(input())
for i in range (n):
    v = input()
    v1 = int(v[0])
    v2 = v[1]
    v3 = int(v[2])
    if(v1 == v3):
        print(v1*v3)
        continue
    if(v2.isupper()):
        print(v3-v1)
        continue 
    print(v1+v3)
    