d = ""
while(d != "S"):
    s = int(input("Forneça o salário do funcionário: "))
    sd = s*0.11
    if(sd > 320):
        print("O desconto será de 320R$")
    else:
        print("O desconto será de {:.2f}".format(sd))
    d = input("Deseja parar? Digite (S)im para parar a execução do sistema ")
