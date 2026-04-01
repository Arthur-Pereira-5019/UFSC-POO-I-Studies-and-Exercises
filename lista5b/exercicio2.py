n1, n2, n3, n4, n5 = input().split()
n1 = float(n1)
me = n1
ma = n1

n2 = float(n2)
if(n2 > ma):
    ma = n2
if(n2 < me):
    me = n2

n3 = float(n3)
if(n3 > ma):
    ma = n3
if(n3 < me):
    me = n3

n4 = float(n4)
if(n4 > ma):
    ma = n4
if(n4 < me):
    me = n4
    
n5 = float(n5)
if(n5 > ma):
    ma = n5
if(n5 < me):
    me = n5
s = n1 + n2 + n3 + n4 + n5
s = s - me - ma
print("{:.1f}".format(s))


