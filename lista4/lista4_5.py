while True:
    v = int(input("Forneça um valor inteiro para calcular sua tabuada, caso o valor seja 0, o código será parado: "))
    if(v == 0):
        break
    else:
        i = 1
        while(i <= 10):
            print("{} x {} = {}".format(i,v,i*v))
            i += 1