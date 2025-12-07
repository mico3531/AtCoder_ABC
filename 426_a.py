X, Y = map(str, input().split())

def ver_func(S):
    if S == "Ocelot":
        return 0
    elif S == "Serval":
        return 1
    elif S == "Lynx":
        return 2
    else:
        print("Another")

ver_x = ver_func(X)
ver_y = ver_func(Y)

if ver_x >= ver_y:
    print("Yes")
else:
    print("No")