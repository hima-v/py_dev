# insertion of elements to binary heap.
h=[]
for j in range (10):
    x=(int(input("Enter any number")))
    h.append(x) 
    i=j
    while i>0 and h[i]<h[(i-1)//2]:
        h[i],h[(i-1)//2]=h[(i-1)//2],h[i]
        i=(i-1)//2
print("The binary heap array format is:",h)
