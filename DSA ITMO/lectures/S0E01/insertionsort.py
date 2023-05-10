def insertion(arr):
    k=0
    a=arr
    n=len(a)
    for i in range(0,n):  #this means i in range 0 to n-1 --> 0,1,2,3 if n=4
        j=i
        while j>0 and a[j]<a[j-1]:
            # print("i count: ",i)
            # print("j count: ",j)
            print("before:",a)
            a[j],a[j-1]=a[j-1],a[j]
            print("after:",a)
            j-=1
            k+=1
    print("total operations elapsed:", k)
    return(a)
arr=[4,3,2,1]
print(insertion(arr))