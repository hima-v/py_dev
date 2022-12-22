def comparision(l_in):
    l1=l_in
    k=0
    if(l1[0]<l1[1] and l1[3]<l1[2] and l1[0]<l1[3] and l1[1]<l1[2]):
        k=1
    return k

def rotation(l_in):
    kemp=l_in[3]
    list_updated=(l_in[:3])
    list_updated.insert(0,kemp)
    return(list_updated,r)

t=int(input())
for i in range (t):
    a,b=map(int,input().split())
    c,d=map(int,input().split())
    l_in=a+b+d+c
    for j in range(4):
        val=comparision(l_in)
        if (val==1):
            print("YES")
            break
        else:
            l_new=rotation(l_in)
            val= comparision(l_new)
            if val==1:
                print("YES")
                break
            
