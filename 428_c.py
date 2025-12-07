Q = int(input())

Ls = [["", 0]]

lefter_count = 0
righter_count = 0
over_index = -1

for _ in range(Q):
    Query = list(map(str, input().split()))
    if Query[0] == "1":
        if Query[1] == "(":
            lefter_count += 1
            Ls.append(["(", lefter_count - righter_count])
        else:
            righter_count += 1
            Ls.append([")", lefter_count - righter_count])
    else:
        last_data = Ls.pop(-1)
        if last_data[0] == "(":
            lefter_count -= 1
        else:
            righter_count -= 1
    
    if over_index == -1 and Ls[-1][1] < 0:
        over_index = len(Ls) - 1
    if over_index > len(Ls) - 1:
        over_index = -1
    
    if over_index == -1 and lefter_count == righter_count:
        print("Yes")
    else:
        print("No")