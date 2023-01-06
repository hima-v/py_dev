def bb(l_ar,base,in_ar):
    st_ar=""
    op_ar="10"
    for ele in in_ar:
        st_ar+=str(ele)
    ar_b=int(st_ar,base)
    for i in range(2,l_ar):
        op_ar=op_ar+str(i)
    op_b=int((op_ar,base))
    return(op_b-ar_b)
t=int(input())
for i in range(t):
    l,b=map(int,input().split())
    ar=list(map(int,input().split()))
    print(bb(l,b,ar))
