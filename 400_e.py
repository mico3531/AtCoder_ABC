import math

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])
            if len(arr) > 2:
                return [[-1, -1]]

    if temp!=1:
        arr.append([temp, 1])
    
    if arr==[]:
        arr.append([n, 1])
    
    if len(arr) > 2:
        return [[-1, -1]]
    
    return arr

Q = int(input())
for _ in range(Q):
    a = int(input())
    b = math.floor(math.sqrt(a)) + 1
    if b**2 > a:
        b -= 1
    while True:
        fact = factorization(b)
        if len(fact) == 2:
            print(b**2)
            break
        b -= 1