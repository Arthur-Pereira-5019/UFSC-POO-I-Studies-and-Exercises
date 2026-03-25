#2
import random
o = random.randint(0,10)
i = False
t = 0
while(not i):
    t += 1
    c = int(input("Digite um valor entre 0 e 10: "))
    if(c != o):
        print("Péssimo chute!")
    else:
        i = True
print("Chute correto! Foram necessárias {} tentativas".format(t))