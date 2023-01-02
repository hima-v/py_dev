# take the second element for sort
def take_second(elem):
    return elem[1]
n=int(input("Enter the number of students"))
nl=[]
for i in range (n):
    nm=input()
    sc=int(input())
    val=[nm,sc]
    nl.append(val)
b=sorted(nl,key=take_second)
print(b)
hh=b[1][1]
print(hh)
print(type(hh))
