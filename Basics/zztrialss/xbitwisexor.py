from functools import reduce
ll=[3,2,2,3]
a=2
b=3
c=4
d=6
e=8
print(a^b) #2,3=1
print(a^c) #2,4=6
print(a^d) #2,6=4
print(a^d) #2,10=4
print(c^d) #4,6=2
print(b^c) #3,4=7
res = reduce(lambda x, y: x ^ y, ll)
print(res)
print(a^a)
print(1^2)