import math
AI = 12
while True:
    e = input()
    if(e == "EOF"):
        break
    D,VF,VG = e.split()
    D = int(D)
    VF = int(VF)
    VG = int(VG)
    # S = S0+V*t
    TAI = (12)/VF
    TPF = D/(VF-VG)
    if(TAI > abs(TPF)):
        print("S")
    else:
        print("N")