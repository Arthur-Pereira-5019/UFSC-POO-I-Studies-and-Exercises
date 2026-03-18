#1
preco = float(input())
parcelas = int(input())
salario = float(input())

vp = preco/parcelas
if(salario*0.3 < vp):
    print("RECUSADO")
else:
    print("APROVADO")
    
#2

vp = int(input())
opcao = input()

match opcao:
    case "a":
        print(vp*0.9)
    case "b":
        print(vp*0.95)
    case "c":
        print(vp)
    case "d":
        print(vp*0.8)
    
#3
peso = float(input())
altura = float(input())
imc = peso / (altura**2)

if(imc > 40):
    print("Obesidade mórbida")
elif(imc > 30):
    print("Obesidade")
elif(imc > 25):
    print("Sobrepeso")
elif(imc > 18.5):
    print("Peso ideal")
else:
    print("Abaixo do peso")

    
#4
n1 = int(input())
n2 = int(input())
n3 = int(input())
media = (n1+n2+n3)/3
if(media < 5):
    print("Reprovado")
elif(5 < media < 7):
    print("Em recuperação")
else:
    print("Aprovado")
    
#5
salario = float(input())

if(salario <= 2000):
    print("Isento")
elif(salario < 3000):
    print("R$ {:.2f}".format(salario*0.92))
elif(salario < 4500):
    print("R$ {:.2f}".format(salario*0.82))
else:
    print("R$ {:.2f}".format(salario*0.72))

#6
    z, d1 = input().split()
h1, z, m1, z, s1 = input().split()

z, d2 = input().split()
h2, z, m2, z, s2 = input().split()

d1 = int(d1)
h1 = int(h1)
m1 = int(m1)
s1 = int(s1)

d2 = int(d2)
h2 = int(h2)
m2 = int(m2)
s2 = int(s2)

sf = 0
mf = 0
hf = 0
df = 0
if(s2 >= s1):
    sf = s2-s1
else:
    sf = 60+s2-s1
    m2 -=1

if(m2 >= m1):
    mf = m2-m1
else:
    mf = 60+m2-m1
    h2 -=1

if(h2 >= h1):
    hf = h2-h1
else:
    hf = 24+h2-h1
    d2 -=1
    
    df = d2-d1
print("{} dia(s)".format(df))
print("{} hora(s)".format(hf))
print("{} minuto(s)".format(mf))
print("{} segundo(s)".format(sf))

#7
ddd = int(input())
match(ddd):
    case 61:
        print("Brasilia")
    case 71:
        print("Salvador")
    case 11:
        print("Sao Paulo")
    case 21:
        print("Rio de Janeiro")
    case 32:
        print("Juiz de Fora")
    case 19:
        print("Campinas")
    case 27:
        print("Vitoria")
    case 31:
        print("Belo Horizonte")
    case _:
        print("DDD nao cadastrado")

#8

m = int(input())
match(m):
    case 1:
        print("January")
    case 2:
        print("February")
    case 3:
        print("March")
    case 4:
        print("April")
    case 5:
        print("May")
    case 6:
        print("June")
    case 7:
        print("July")
    case 8:
        print("August")
    case 9:
        print("September")
    case 10:
        print("October")
    case 11:
        print("November")
    case 12:
        print("December")

#9
        a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)
d = (b**2) - (4*a*c)
if(d < 0):
    print("Impossível de calcular")
else:
    r1 = (-b+d**(1/2))/(2*a)
    r2 = (-b-d**(1/2))/(2*a)
    print("R1: {:.5f}".format(r1))
    print("R2: {:.5f}".format(r2))

#10
    a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

if(a > b > c):
    print(b)
elif(c > b > a):
    print(b)
elif(a > c > b):
    print(c)
elif(b > c > a):
    print(c)
elif(b > a > c):
    print(a)
elif(c > a > b):
    print(a)

#11
    cv, ce, cs, fv, fe, fs = input().split()

cv = int(cv)
ce = int(ce)
cs = int(cs)
fv = int(fv)
fe = int(fe)
fs = int(fs)

cp = cv * 3 + ce
fp = fv * 3 + fe

if(cp > fp or cs > fs):
    print("C")
elif(cp < fp or cs < fs):
    print("F")
else:
    print("=")
    
#12
n = int(input())
l1 = int(input())
l2, l3, l4, l5 = input().split()
l2 = int(l2)
l3 = int(l3)
l4 = int(l4)
l5 = int(l5)
l6 = int(input())
if(l1+l6 == 7 and l2 + l4 == 7 and l3 + l5 == 7):
    print("SIM")
else:
    print("NAO")

#13/14?
    h1, h2 = input().split()
h1 = int(h1)
h2 = int(h2)
if(h1 == h2):
    t = 24
elif(h2 > h1):
    t = h2-h1
else:
    t = 24+h2-h1

print("O JOGO DUROU {} HORA(S)".format(t))

#15
h1, m1, h2, m2 = input().split()
h1 = int(h1)
h2 = int(h2)
m1 = int(m1)
m2 = int(m2)

mf = 0
hf = 0
if(m2 >= m1):
    mf = m2-m1
else:
    mf = 60+m2-m1
    h2-=1

if(h2 >= h1):
    hf = h2-h1
else:
    hf = 24+h2-h1

print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(hf,mf))

#16
d = int(input())
a, l, p = input().split()
a = int(a)
l = int(l)
p = int(p)

if(d > a or d > l or d > p):
    print("N")
else:
    print("S")
    

#17
s = int(input())
t = 0
if(s <= 400):
    t = 15
elif(s <= 800):
    t = 12
elif(s <= 1200):
    t = 10
elif(s <= 2000):
    t = 7
else:
    t = 4

r = s*(t*0.01)
s = s+r
print("Novo salário: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: {} %".format(s,r,t))
       
#18
c1, c2, c3 = input().split()
c1 = int(c1)
c2 = int(c2)
c3 = int(c3)
p1, p2 = input().split()
p1 = int(p1)
p2 = int(p2)

maiorp = p1
menorp = p2
if(p2 > p1):
  maiorp = p2
  menorp = p1
maiorc = c1
menorc = c2

if(c1 > c2):
    if(c3 > c1):
        maiorc = c1
        menorc = c2
    elif(c3 > c2):
        maiorc = c3
        menorc = c2
    else:
        maiorc = c2
        menorc = c3
else:
    if(c3 > c2):
        maiorc = c2
        menorc = c1
    elif(c3 > c1):
        maiorc = c3
        menorc = c1
    else:
        maiorc = c1
        menorc = c3

if(maiorp >= maiorc && menorp >= menorc):
    print("S")
else:
    print("N")

#19
    A, B, C, D = input().split()
A = int(A)
B = int(B)
C = int(C)
D = int(D)

if(B > C and D > A and C+D > A+B and C > 0 and D > 0 and A%2==0):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")

#20
C, Q = input().split()
C = int(C)
Q = int(Q)
p = 0.0
if(C == 1):
    p = 4
elif(C == 2):
    p = 4.5
elif(C == 3):
    p = 5
elif(C == 4):
    p = 2
else:
    p = 1.5

print("Total: R$ {:.2f}".format(p*Q))
    
#21
P, C, Q = input().split()
P = int(P)
C = int(C)
Q = int(Q)
if(Q*P <= C):
    print("S")
else:
    print("N")
    

