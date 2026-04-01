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
    TAI = (12)/VF
    TPF = (((D**2)+(AI**2))**1/2)/VG
    if(TAI > TPF):
        print("S")
    else:
        print("N")