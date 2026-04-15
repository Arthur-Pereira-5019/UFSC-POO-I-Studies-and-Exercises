n = int(input())
for i in range (n):
    v = input()
    leds = 0
    for j in range (len(v)):
        if(v[j] == "1"):
            leds += 2
        elif(v[j] == "2"):
            leds += 5
        elif(v[j] == "3"):
            leds += 5
        elif(v[j] == "4"):
            leds += 4
        elif(v[j] == "5"):
            leds += 5
        elif(v[j] == "6"):
            leds += 6
        elif(v[j] == "7"):
            leds += 3
        elif(v[j] == "8"):
            leds += 7
        elif(v[j] == "9"):
            leds += 6
        elif(v[j] == "0"):
            leds += 6
    print("{} leds".format(leds))