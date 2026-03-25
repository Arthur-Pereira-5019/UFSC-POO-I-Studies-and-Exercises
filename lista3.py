#1
for i in range(2001,2100):
    if(i%4==0):
        print(i)

#2
for i in range(1,50):
    if(i%2==1):
        print(i)

#3
mnome = ""
mnota = 0
mvm = 0
for i in range(1,6):
    nome = input("Forneça o nome do aluno: ")
    nota = float(input("Forneça a sua nota: "))
    vm = float(input("Forneça o valor da mensalidade fornecida: "))
    if(nota == mnota):
        i -= 1
    if(nota > mnota):
        mnota = nota
        mnome = nome
        mvm = vm

print("Os dados do aluno selecionado são:")
print("Nome: {}".format(mnome))
print("Nota: {}".format(mnota))
print("Valor sem desconto: R$ {:.2f}".format(mvm))
print("Valor com desconto: R$ {:.2f}".format(mvm*0.7))
    
    
#4
np = 0
ni = 0
for i in range(0,10):
    n = int(input())
    if(n%2==0):
        np += 1
    else:
        ni += 1
print("No total, foram {} pares e {} ímpares".format(np,ni))

#5
n = int(input())
divisores = ""
a = False
if(n == 1):
    print("O número nao é primo!")
else:
    for j in range(2,n):
        if(n % j == 0):
            print("O número nao é primo!")
            a = True
            break;
    if(not a):
        print("O número é primo!")

#6
n = int(input())
divisores = ""
for j in range(2,n):
    if(n % j == 0):
        divisores = divisores + str(j) + ", "
    if(divisores != ""):
        print("O número nao é primo e é divisível por: " + divisores)
    elif(n == 1):
        print("O número nao e primo!")
    else:
        print("O número é primo!")
        
#7
n = int(input())
mp = 0
for i in range(0,n):
    mp += int(input("Forneça a sua idade: "))
if(mp/n < 25):
    print("Jovem")
elif(mp/n < 60):
    print("Adulta")
else:
    print("Idosa")

#8
    n = int(input())
m = int(input())

sp = 0
pp = 1
for i in range(n,m+1):
    print(i)
    sp += i
    pp = pp * i

print(sp)
print(pp)

#9
n = int(input())
for i in range (1,11):
    print("{} x {} = {}".format(n,i,n*i))


#10
mn = 0
amn = ""
mp = 0
for i in range(0,5):
    nomeAluno = input("Forneça o nome do aluno: ")
    nota = int(input("Forneça a nota do aluno: "))
    mp += nota
    if(nota > mn):
        mn = nota
        amn = nomeAluno

mt = mp/5
s = ""
if(mn >= 5.75):
    s = "Aprovado"
elif(mn >= 2.75):
    s = "Em recuperação"
else:
    s = "Reprovado"
print("A média da turma é {}, o aluno com a melhor nota é {}, sua nota é {} e ele está {}".format(mt,amn,mn,s))

#11
n = int(input())
mp = 0
ma = 0
me = 0
for i in range (0,n):
    v = int(input())
    mp +=v
    if(i == 1):
        ma = v
        me = v
    else:
        if(v > ma):
            ma = v
        elif(v < me):
            me = v
mt = mp/n
print("A média dos valores fornecidos é {}, o maior deles informado é {} e o menor {}".format(mt,ma,me))

#12
n = int(input())
ml = 0
mp = 0
fe = 0
pmd = ""
for i in range (n):
    s = input("Forneça o nome da praia: ")
    d = int(input("Forneça a distância da praia: "))
    mp += d
    if(d > ml):
        ml = d
        pmd = s
    if(15 <= d <= 20):
        fe += 1

mt = mp/n
print("A praia mais distante é a {}, à {:.1f}Km, existem no total {} localizadas entre 15Km e 20Km, por fim, a média entre as praias é de {:.1f}KM".format(pmd,ml,fe,mt))
