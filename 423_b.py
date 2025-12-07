N = int(input())
L = list(map(int, input().split()))

state = [0 for _ in range(N+1)]
state[0] = 1
state[-1] = 1
for i in range(N):
    if state[i] == 1 and L[i] == 0:
        state[i+1] = 1
for i in range(N, 0, -1):
    if state[i] == 1 and L[i-1] == 0:
        state[i-1] = 1

print(N+1 - sum(state))