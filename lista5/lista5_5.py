n = int(input())
q = 0
for i in range (0,n):
    A,B = input().split()
    A = int(A)
    B = int(B)
    if(A > B):
        q += B
print(q)