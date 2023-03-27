for i in range(int(input())):
    l=int(input())
    st=input()
    rev=st[::-1]
    k=0
    j=0
    for j in range(l//2):
        if(int(st[j])^int(rev[j])==0):
            break
        else:
            k+=1
    if l>1:
        if (k==l//2) and k!=1: print(0)
        elif k==1:
            print(l-2)
        else: print(l-(2*k))
    elif l==1:
        print(1)
    # if j>0 and l>1 and j<l//2: print(l-(2*j))
    # elif j==l//2: print(0)
    # elif j==0 and k==1: print(l-2)
    # elif j==0 and k==0 and l==1: print(0)
    # else: print(l)