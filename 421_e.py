condition_set = set()

for i in range(7 ** 5):
    Ls = [0 for _ in range(7)]
    for _ in range(5):
        ind = i % 7
        Ls[ind] += 1
        i //= 7
    num = 0
    for j in range(7):
        num *= 10
        num += Ls[j]
    condition_set.add(num)

print(len(condition_set))
print(condition_set)

condition_list = list(condition_set)
E = [0 for _ in range(462)]

A = list(map(int, input().split()))

def score(X):
    ret = 0
    for i in range(5):