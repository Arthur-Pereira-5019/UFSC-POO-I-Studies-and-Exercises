#1
v = False
s = ""
while(not v):
    s = input("Digite seu sexo: ")
    if(s != "M" and s != "F"):
        print("Sexo inválido, forneça um sexo no formato M ou F")
    else:
        v = True
print("O sexo fornecido foi",s)