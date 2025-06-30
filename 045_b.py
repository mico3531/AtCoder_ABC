SA = str(input())
SB = str(input())
SC = str(input())

a, b, c = 0, 0, 0
x = "a"
check = True
while check:
    if x == "a":
        if a == len(SA):
            check = False
            print("A")
        else:
            x = SA[a]
            a += 1
        # print("A")
    elif x == "b":
        if b == len(SB):
            check = False
            print("B")
        else:
            x = SB[b]
            b += 1
        # print("B")
    else:
        if c == len(SC):
            check = False
            print("C")
        else:
            x = SC[c]
            c += 1
        # print("C")
