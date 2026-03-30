N,S = input().split()
N = int(N)
S = int(S)
ms = S
for i in range (N):
    a = int(input())
    S += a
    if(S < ms):
        ms = S
print(ms)