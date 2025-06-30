N = int(input())

i = 0
score = 0
while score < N:
    i += 1
    score += i

# print(i)

if score == N:
    for x in range(1, i+1):
        print(x)
else:
    NG = score - N
    for x in range(1, i+1):
        if x != NG:
            print(x)