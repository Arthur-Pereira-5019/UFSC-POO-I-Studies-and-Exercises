n = int(input())
qc = 0
qs = 0
qr = 0
t = 0
for i in range (n):
    q,a = input().split()
    q = int(q)
    t += q
    if(a == "C"):
        qc += q
        continue
    if(a == "S"):
        qs += q
        continue
    qr += q
    
print("Total: {} cobaias".format(t))
print("Total de coelhos: {}".format(qc))
print("Total de ratos: {}".format(qr))
print("Total de sapos: {}".format(qs))
print("Percentual de coelhos: {:.2f} %".format((qc/t)*100))
print("Percentual de ratos: {:.2f} %".format((qr/t)*100))
print("Percentual de sapos: {:.2f} %".format((qs/t)*100))

