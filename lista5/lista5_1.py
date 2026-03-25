j1 = input("Jogador 1! Fale sua jogada (Pedra, Papel, Tesoura) ")
j2 = input("Jogador 2! Fale sua jogada (Pedra, Papel, Tesoura) ")
if(j1 == j2):
    print("Empate")
else:
    if(j1 == "Pedra" and j2 == "Papel"):
        print("Vitória do jogador 2")
    elif(j1 == "Papel" and j2 == "Pedra"):
        print("Vitória do jogador 1")
    elif(j1 == "Tesoura" and j2 == "Pedra"):
        print("Vitória do jogador 2")
    elif(j1 == "Pedra" and j2 == "Tesoura"):
        print("Vitória do jogador 1")
    elif(j1 == "Tesoura" and j2 == "Papel"):
        print("Vitória do jogador 1")
    elif(j1 == "Papel" and j2 == "Tesoura"):
        print("Vitória do jogador 2")