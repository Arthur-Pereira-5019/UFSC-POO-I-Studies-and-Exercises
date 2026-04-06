def contador(ini,fim,passo):
    if(ini > fim):
        passo = 0 - passo
    for i in range (ini,fim,passo):
        print(i)

contador(1,10,1)
contador(10,0,2)
contador(20,5,5)