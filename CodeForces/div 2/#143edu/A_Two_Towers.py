t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    s = input()
    t = input()
    bigt = s + t
    end=n+m-2
    for i in range (2,n+m-2):
        st=bigt[:i]
        endg=bigt[i:]
        for j in range(1,max(len(st),len(endg))):
            if st[j]!=st[j-1]:
                if end[j]!=end[j-1]:
                    continue
                
    # for j in range(1, n+m):
    #     if bigt[j] == bigt[j-1]:
    #         print("NO")
    #         break
    # else:
    #     print("YES")
