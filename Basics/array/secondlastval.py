n = int(input())
arr = map(int, input().split())
a=sorted(arr, reverse=True)
maxi=a[0]
for i in range (1,n+1):
        if (a[i]<maxi):
            print(a[i])
            break
        else:
            continue