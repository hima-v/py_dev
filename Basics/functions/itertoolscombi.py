from itertools import combinations
n=8
solnspace=[]
for i in range (1,7): 
    for j in range (1,n+1):
        solnspace.append(i)
# size of combination is set to 3
a = list(set((combinations(solnspace, 3))))
y = [sum(i) for i in a]
print(a)
print(y)
if(y[1]==7):
    print(a[1])
# [1,2,3]*[1,2,3]=[(1,1),(1,2),(1,3)]