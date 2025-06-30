S = str(input())
N = len(S)

ans = "Yes"

if N % 2 != 0:
    ans = "No"
else:
    Kind = set()
    for i in range(0, N-1, 2):
        if S[i] != S[i + 1]:
            ans = "No"
        elif S[i] in Kind:
            ans = "No"
        else:
            Kind.add(S[i])

print(ans)