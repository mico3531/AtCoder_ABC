W, B = map(int, input().split())

W *= 1000
n = W // B
while n*B <= W:
    n += 1
print(n)