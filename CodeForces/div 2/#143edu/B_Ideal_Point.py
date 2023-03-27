t = int(input())
rgs=[]
for _ in range(t):
    n, k = map(int, input().split())
    for i in range(n):
        l, r = map(int, input().split())
        rgs.append([l,r])
    def idealpt(rgs):
        count = [0] * 51
        for inl in rgs:
            count[inl[0]] += 1
            count[inl[1]+1] -= 1
        prefix_sum = [0] * 51
        for i in range(1, 51):
            prefix_sum[i] = prefix_sum[i-1] + count[i]
        maxfrequency=max(prefix_sum)
        if prefix_sum[k] == max(prefix_sum) and prefix_sum.count(prefix_sum[k]) == 1:
            print("YES")
        else:
            if k in maxfrequency: maxfrequency.remove[k]
            el=maxfrequency[0]
            for listvals in rgs:
                if el<=listvals[1] and el>=listvals[0] and k>listvals[1] and k<listvals[0]:
                    rgs.remove[listvals]
                    print(rgs)
            print("NO")
