import math

def solve():
    TS_x, TS_y, TG_x, TG_y = map(int, input().split())
    AS_x, AS_y, AG_x, AG_y = map(int, input().split())

    sq_dist_T = (TS_x - TG_x) ** 2 + (TS_y - TG_y) ** 2
    sq_dist_A = (AS_x - AG_x) ** 2 + (AS_y - AG_y) ** 2

    dist_T = math.sqrt(sq_dist_T)
    dist_A = math.sqrt(sq_dist_A)

    TE_x = (TG_x - TS_x) / dist_T
    TE_y = (TG_y - TS_y) / dist_T
    AE_x = (AG_x - AS_x) / dist_A
    AE_y = (AG_y - AS_y) / dist_A

    def point_T(t):
        if t <= dist_T:
            return TS_x + t * TE_x, TS_y + t * TE_y
        else:
            return TG_x, TG_y
    
    def point_A(t):
        if t <= dist_A:
            return AS_x + t * AE_x, AS_y + t * AE_y
        else:
            return AG_x, AG_y
    
    def dist(t):
        x_T, y_T = point_T(t)
        x_A, y_A = point_A(t)

        sq = (x_T - x_A) ** 2 + (y_T - y_A) ** 2
        return math.sqrt(sq)

    L = 0
    R = min(dist_T, dist_A)
    while R-L > 1e-10:
        lefter = (2*L + R) / 3
        righter = (L + 2*R) / 3
        if dist(lefter) < dist(righter):
            R = righter
        else:
            L = lefter
        # print("1", L, R)
    ans = dist(L)

    L = min(dist_T, dist_A)
    R = max(dist_T, dist_A)
    while R-L > 1e-10:
        lefter = (2*L + R) / 3
        righter = (L + 2*R) / 3
        if dist(lefter) < dist(righter):
            R = righter
        else:
            L = lefter
        # print("2", L, R)
    ans = min(ans, dist(L))
    
    print("{:.10f}".format(ans))
    return 0

T = int(input())
for _ in range(T):
    solve()