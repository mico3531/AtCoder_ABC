A = list(map(int,input().split()))
Count = [0 for _ in range(14)]
for i in range(7):
    Count[A[i]] += 1

count_2 = 0
count_3 = 0
for i in range(14):
    if Count[i] >= 2:
        count_2 += 1
    if Count[i] >= 3:
        count_3 += 1

# print(Count)

if count_2 >= 2 and count_3 >= 1:
    print("Yes")
else:
    print("No")