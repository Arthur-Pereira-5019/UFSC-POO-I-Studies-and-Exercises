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
