nums = list(map(int, input().split()))

nums.sort()
ans = 100 * nums[2] + 10 * nums[1] + nums[0]

print(ans)