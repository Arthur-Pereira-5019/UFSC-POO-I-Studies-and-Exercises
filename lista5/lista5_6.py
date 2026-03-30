A, B, C, D = input().split()
A = float(A)
B = float(B)
C = float(C)
D = float(D)

a = A*C
g = B*D
if(a >= g):
    print("G")
else:
    print("A")