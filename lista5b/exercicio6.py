n = float(input())
A = n//100
n = n - A*100
B = n//50
n = n - B*50
C = n//20
n = n - C*20
D = n//10
n = n - D*10
E = n//5
n = n - E*5
F = n//2
n = n - F*2


G = n//1
n = n - G*1
H = n//0.5
n = n - H*0.5
I = n//0.25
n = n - I*0.25
J = n//0.1
n = n - J*0.1
K = n//0.05
n = n - K*0.05
L = n//0.01
n = n - L*0.01

print("NOTAS:\n{} nota(s) de R$ 100.00\n{} nota(s) de R$ 50.00\n{} nota(s) de R$ 20.00\n{} nota(s) de R$ 10.00\n{} nota(s) de R$ 5.00\n{} nota(s) de R$ 2.00\nMOEDAS:\n{} moeda(s) de R$ 1.00\n{} moeda(s) de R$ 0.50\n{} moeda(s) de R$ 0.25\n{} moeda(s) de R$ 0.1\n{} moeda(s) de R$ 0.05\n{} moeda(s) de R$ 0.01".format(int(A),int(B),int(C),int(D),int(E),int(F),int(G),int(H),int(I),int(J),int(K),int(L)))
