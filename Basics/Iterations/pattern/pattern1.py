#print a pattern
i=1
j=1
print(j)
def iter(i,j):
    while j<i:
        return(j,iter(i,j+1))
for i in range(1,6):
    for j in range(i+1):
        while(j<i):
            print(iter(i,j))
            break

