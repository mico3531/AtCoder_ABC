a, b, x = map(int,input().split())

k = (a // x) * x
l = (b // x) * x

while k < a:
    k += x
while l+x <= b:
    l += x

print(1 + (l-k) // x)