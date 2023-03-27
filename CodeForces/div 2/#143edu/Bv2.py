t = int(input())
d={}
for _ in range(t):
    n, k = map(int, input().split())
    count = [0] * 51
    for i in range(n):
        l, r = map(int, input().split())
        d[i]=[l,r]
        count[l] += 1
        count[r+1] -= 1
    prefix_sum = [0] * 51
    for i in range(1, 51):
        prefix_sum[i] = prefix_sum[i-1] + count[i]
    if prefix_sum[k] == max(prefix_sum) and prefix_sum.count(prefix_sum[k]) == 1:
        print("YES")
    else:
        print("NO")