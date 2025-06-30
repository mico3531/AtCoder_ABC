N = int(input())
A = list(map(int,input().split()))

count4 = 0
count1 = 0

for i in range(N):
    if A[i] % 4 == 0:
        count4 += 1
    elif A[i] % 2 != 0:
        count1 += 1

if count4 >= count1:
    print("Yes")
elif count4 + 1 == count1 and count4 + count1 == N:
    print("Yes")
else:
    print("No")