N, K = map(int,input().split())
S = list(str(input()))

for i in range(1, N):
    if S[i-1] == "o" and S[i] == "?":
        S[i] = "."

for i in range(N-1, 0, -1):
    if S[i] == "o" and S[i-1] == "?":
        S[i-1] = "."

# print(S)

max_count = 0
cont_size = 0
for i in range(N):
    if S[i] == "?":
        if cont_size > 0:
            cont_size += 1
        else:
            cont_size = 1
    else:
        if cont_size > 0:
            # print(cont_size)
            max_count += (cont_size + 1) // 2
            cont_size = 0

if cont_size > 0:
    # print(cont_size)
    max_count += (cont_size + 1) // 2

o_count = 0
for i in range(N):
    if S[i] == "o":
        o_count += 1

# print(o_count, max_count)

K -= o_count
# print(K, max_count)

T = ["" for _ in range(N)]

if K == 0:
    for i in range(N):
        if S[i] == "?":
            T[i] = "."
        else:
            T[i] = S[i]

elif K == max_count:
    T = ["" for _ in range(N)]
    l = -1
    for i in range(N):
        if l == -1:
            if S[i] == "?":
                l = i
            else:
                T[i] = S[i]
        else:
            if S[i] != "?":
                r = i
                # print(l, r)
                if (r-l) % 2 == 0:
                    for j in range(l, r):
                        T[j] = "?"
                else:
                    for j in range(l, r):
                        if j % 2 == l % 2:
                            T[j] = "o"
                        else:
                            T[j] = "."
                l = -1
                T[i] = S[i]
    if l != -1:
        r = N
        if (r-l) % 2 == 0:
            for j in range(l, r):
                T[j] = "?"
        else:
            for j in range(l, r):
                if j % 2 == l % 2:
                    T[j] = "o"
                else:
                    T[j] = "."

else:
    T = S

print("".join(T))