A = int(input())
N = int(input())

def base_a(x) -> str:
    str_a = ""
    while x:
        if x % A >= 10:
            return "-1"
        str_a += str(x % A)
        x //= A
    return str_a[::-1]

ans = 0
for i in range(10 ** 6):
    s = str(i)
    rev_s = s[::-1]
    num_1 = s + rev_s
    num_2 = s[:-1] + rev_s
    # print(num_1)
    # print(num_2)

    changed_1 = base_a(int(num_1))
    changed_1_rev = changed_1[::-1]
    if changed_1 == changed_1_rev and int(num_1) <= N:
        ans += int(num_1)
    
    changed_2 = base_a(int(num_2))
    changed_2_rev = changed_2[::-1]
    if changed_2 == changed_2_rev and int(num_2) <= N:
        ans += int(num_2)

print(ans)