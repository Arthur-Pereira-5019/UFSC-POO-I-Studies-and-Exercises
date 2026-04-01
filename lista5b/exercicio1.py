M,N = input().split()
M = int(M)
N = int(N)
i = 0

while True:
    i += 1
    r = ((N*i) - (M*i))
    if(r > N):
        break
print(i)