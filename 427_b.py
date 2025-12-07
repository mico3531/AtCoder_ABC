N = int(input())

A = [0 for _ in range(200)]
A[1] = 1

def f(x):
    s = str(x)
    ret = 0
    for i in range(len(s)):
        ret += int(s[i])
    return ret

for i in range(2, 200):
    for j in range(1, i):
        A[i] += f(A[j])

# print(A)
print(A[N+1])