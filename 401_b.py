N = int(input())
log_in = False
count = 0
for _ in range(N):
    S = str(input())
    if not log_in and S == "private":
        count += 1
    elif S == "login":
        log_in = True
    elif S == "logout":
        log_in = False

print(count)