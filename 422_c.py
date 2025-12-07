T = int(input())

for _ in range(T):
    a, b, c = map(int, input().split())
    ans_1 = (a+b+c) // 3
    ans_2 = min(a, c)
    print(min(ans_1, ans_2))