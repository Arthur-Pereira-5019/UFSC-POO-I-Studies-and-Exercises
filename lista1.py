'''
Lista de Exercicios 1
 Turma – 01208A Aluno – Arthur Pereira 
'''

#1003
A = int(input())
B = int(input())
soma = str(A+B);
print("SOMA " + "= " + soma)


#1004
A = int(input())
B = int(input())
produto = str(A*B);
print("PROD " + "= " + produto)


#1005
A = float(input())
B = float(input())
media = (A+B)/2;
print("MEDIA = {:.5f}".format(media))


#1006
A = float(input())
B = float(input())
C = float(input())
media = (A*2+B*3+C*5)/10;
print("MEDIA = {:.1f}".format(media))


#1007
A = int(input())
B = int(input())
C = int(input())
D = int(input())
dif = (A*B)-(C*D);
print("DIFERENCA = {}".format(dif))


#1008
numero = int(input())
horas = int(input())
base = float(input())
salario = horas*base
print("NUMBER = {}".format(numero))
print("SALARY = U$ {:.2f}".format(salario))


#2374
N = int(input())
M = int(input())
dif = str(N-M);
print(dif)


#2413
t = int(input())
print(t*4)


#1012
A, B, C = input().split()
A = int(A)
B = int(B)
C = int(C)

print("TRIANGULO: {:.3f}".format(A*B/2))
print("CIRCULO: {:.3f}".format(C*3.14159))
print("TRAPEZIO: {:.3f}".format(((A+B)*C)/2))
print("QUADRADO: {:.3f}".format(B*B))
print("RETANGULO: {:.3f}".format(A*B))


#1020
i = int(input())
a = i//365
i -= a*365
m = i//30
i -= m*30
d = i
i -= d
print("{} ano(s)".format(a))
print("{} mes(es)".format(m))
print("{} dia(s)".format(d))


#1015
x1, y1 = input().split()
x1 = float(x1)
y1 = float(y1)

x2, y2 = input().split()
x2 = float(x2)
y2 = float(y2)
distancia = ((x2-x1)**2 + (y2-y1)**2)**(1/2)
print("{:.4f}".format(distancia))


#1019
n = int(input())

h = n//3600
n = n - h*3600

m = n//60
n = n - m*60

s = n

print("{}:{}:{}".format(h,m,s))


#1017

h = int(input())
v = int(input())
print("{:.3f}".format((h*v)/12))


#1014

X = int(input())
Y = int(input())
print("{:.f} km/l".format(X/Y))


#1009

nome = input()
salario = float(input())
vendas = float(input())
print("TOTAL = {:.2f}".format(salario + (vendas*0.15)))



