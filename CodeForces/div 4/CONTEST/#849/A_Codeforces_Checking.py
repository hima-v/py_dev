w="codeforces"
for i in range(int(input())):
    k=0
    c=str(input())
    for j in range(10):
        if(w[j]==c):
            k=1
            break
    if(k==1):
        print("YES")
    else:
        print("NO")
