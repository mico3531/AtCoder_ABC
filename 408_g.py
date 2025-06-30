import math

T = int(input())

for _ in range(T):
    A, B, C, D = map(int, input().split())
    uplim = math.floor((B*D)/(B*C - A*D)) + 1
    print("uplim is", uplim)