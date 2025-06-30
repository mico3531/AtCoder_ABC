S = str(input())
L = len(S)

def dig_sum(x):
    count = 0
    for j in range(10):
        y = x // (10 ** j)
        count += (y % 10)
    return count

if len(S) <= 5:
    N = int(S)
    check = False
    for i in range(N, 2*N):
        count1 = dig_sum(i)
        count2 = dig_sum(i+1)
        if i % count1 == 0 and (i+1) % count2 == 0:
            ans = i
            check = True
            break
    if check:
        print(ans)
    else:
        print(-1)
else:
    if S[0] == "1":
        check = True
        for i in range(1, L):
            if S[i] != "0":
                check = False
        if check:
            print( "1" + "0" * (L-3) + "10" )
        else:
            print( "2" + "0"*(L-1) )
    elif S[0] == "2":
        print( "3" + "0"*(L-3) + "32" )
    elif S[0] == "3":
        print( "4" + "0"*(L-3) + "40")
    elif S[0] == "4" or S[0] == "5":
        print( "62" + "0" * (L-2) )
    else:
        print( "1" + "0" * (L-2) + "10" )