N = int(input())
S = str(input())

if len(S) < 3:
    print("No")
else:
    if S[-3:] == "tea":
        print("Yes")
    else:
        print("No")