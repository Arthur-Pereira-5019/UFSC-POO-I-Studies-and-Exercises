n1 = int(input())
n2 = int(input())
n3 = int(input())
print("Ordenando...")
if(n1 < n2 < n3):
    print("A ordem é {} {} {}".format(n1,n2,n3))
elif(n1 < n3 < n2):
    print("A ordem é {} {} {}".format(n1,n3,n2))
elif(n2 < n1 < n3):
    print("A ordem é {} {} {}".format(n2,n1,n3))
elif(n2 < n3 < n1):
    print("A ordem é {} {} {}".format(n2,n3,n1))
elif(n3 < n2 < n1):
    print("A ordem é {} {} {}".format(n3,n2,n1))
elif(n3 < n1 < n2):
    print("A ordem é {} {} {}".format(n3,n1,n2))
