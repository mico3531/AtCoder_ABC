from collections import deque

def solve():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    
    Ans = [[0 for _ in range(M)] for _ in range(N)]
    
    pre_Queue = []
    Count = [0 for _ in range(N*M + 1)]

    for i in range(N):
        pre_Queue.append([X[i], "x", i])
        Count[X[i]] += 1
    for j in range(M):
        pre_Queue.append([Y[j], "y", j])
        Count[Y[j]] += 1
    pre_Queue.sort()
    Queue = deque(pre_Queue)

    posi_Queue = deque([])
    # print("Test start")
    # print(Queue)

    num = N*M

    if max(Count) > 2:
        print("No")
        return 0

    while num > 0:
        if Count[num] == 2:
            data_1 = Queue.pop()
            data_2 = Queue.pop()
            # print(data_1, data_2)
            y = data_1[2]
            x = data_2[2]
            if data_1[1] == data_2[1]:
                print("No")
                return 0
            Ans[x][y] += num + 2
            for i in range(N):
                Ans[i][y] -= 1
                if Ans[i][y] == -2:
                    posi_Queue.append([i, y])
            for j in range(M):
                Ans[x][j] -= 1
                if Ans[x][j] == -2:
                    posi_Queue.append([x, j])
        
        elif Count[num] == 1:
            data = Queue.pop()
            if data[1] == "x":
                x = data[2]
                changed = False
                for j in range(M):
                    Ans[x][j] -= 1
                    if Ans[x][j] == -2:
                        if changed:
                            posi_Queue.append([x, j])
                        else:
                            Ans[x][j] += num + 2
                            changed = True
            else:
                y = data[2]
                changed = False
                for i in range(N):
                    Ans[i][y] -= 1
                    if Ans[i][y] == -2:
                        if changed:
                            posi_Queue.append([i, y])
                        else:
                            Ans[i][y] += num + 2
                            changed = True
        
        else:
            if len(posi_Queue) > 0:
                posi = posi_Queue.popleft()
                x = posi[0]
                y = posi[1]
                Ans[x][y] += num + 2
            else:
                print("No")
                return -1
        
        num -= 1
    
    for i in range(N):
        max_num = 0
        for j in range(M):
            max_num = max(max_num, Ans[i][j])
        if max_num != X[i]:
            print("No")
            return 0
    
    for j in range(M):
        max_num = 0
        for i in range(N):
            max_num = max(max_num, Ans[i][j])
        if max_num != Y[j]:
            print("No")
            return 0

    print("Yes")
    for i in range(N):
        print(* Ans[i])
    return 0

T = int(input())
for _ in range(T):
    solve()