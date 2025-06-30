import math
import bisect

# 8乗は37以下
pls1 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
for i in range(len(pls1)):
    pls1[i] = pls1[i] ** 8

# 2乗は10**6以下
def prime(n):
    is_prime = [True] * (n + 1)
    is_prime[0], is_prime[1] = False, False
    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime[i]:
            for j in range(2 * i, n + 1, i):
                is_prime[j] = False
    return is_prime

# 素数列挙
M = 10 ** 6
# M以下の整数の素数判定
prime = prime(M)

# 素数判定を基に, 素数リストを作成
pls2 = []
for i in range(M + 1):
    if prime[i]:
        pls2.append(i)
for i in range(len(pls2)):
    pls2[i] = pls2[i] ** 2

N = int(input())

ans = 0
for i in range(len(pls1)):
    if pls1[i] <= N:
        ans += 1
# print(ans)

i = 0
j = len(pls2)-1

while i < len(pls2):
    while j >= 1 and pls2[i] * pls2[j] > N:
        j -= 1
    if j > i:
        ans += j-i
    i += 1

print(ans)