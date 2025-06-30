N, M = map(int,input().split())

def MD( p1, p2 ):
    D = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    return D

Student = []
for i in range(N):
    a, b = map(int,input().split())
    Student.append([a,b])

Point = []
for j in range(M):
    c, d = map(int,input().split())
    Point.append([c, d])

for i in range(N):
    D = float("inf")
    for j in range(M):
        D = min( D, MD(Student[i], Point[j]) )
    for j in range(M):
        if D == MD(Student[i], Point[j]):
            print(j+1)
            break
