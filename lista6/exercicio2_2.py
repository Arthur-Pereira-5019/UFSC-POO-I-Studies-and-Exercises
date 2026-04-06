def aumento_salario(sal):
    if(sal <= 400):
        r = 0.15
    elif(sal <= 800):
        r = 0.12
    elif(sal <= 1200):
        r = 0.1
    elif(sal <= 2000):
        r = 0.07
    else:
        r = 0.04
    vr = sal*r
    sca = sal+vr
    print("Novo salário: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: {}%".format(sca,vr,r*100))
aumento_salario(400)