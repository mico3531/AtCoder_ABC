N, M = map(int,input().split())

if M == 1 and N == 1:
    print(1)
elif min(N, M) == 1:
    print( max(0, N*M - 2) )
else:
    print( (N-2) * (M-2) )
