N = int(input())

ans = "-" * ((N-1)//2) + "=" * (2 - (N % 2)) + "-" * ((N-1)//2)
print(ans)