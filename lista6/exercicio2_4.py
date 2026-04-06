S = 0
T = 0
F = 0
def verifica_entrada():
    if(not (0 <= S <= 23)):
       return False
    if(not (1 <= T <= 12)):
       return False
    if(not (-5 <= F <= 5)):
       return False
    return True

def fuso(s,t,f):
    cp = s + t
    if (t+s > 23):
        cp = t+s-24
    cp = cp+f
    print(cp)
        

while(not verifica_entrada()):
    S,T,F = input().split()
    S = int(S)
    T = int(T)
    F = int(F)
fuso(S,T,F)
