# Combinations Of string "GeEKS" OF SIZE 3.


from itertools import combinations

letters =[1,2,3,4,5,6]

# size of combination is set to 3
a = list(combinations(letters, 3))
y = [sum(i) for i in a]
print(y)
if(y[1]==7):
    print(a[1])
