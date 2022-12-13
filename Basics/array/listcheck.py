#even if list has same first and last elements, 
#the function isnt detecting logic in listelements
l1=[10,20,20,40]
l2=[10,40,80,100]
l3=[20,40,60,20]
x=len(l3)
print(l3[0])
print(l3[x-1])
def listelements(list):
    n=len(list)
    print(list)
    if(l1[0]==l1[n-1]):
        print("The list has first element and last element same")
    else:
        print("The first and last elements of the list are not same")

def listcomparision(a,b):
    print(a)
    print(b)
    n1=len(a)
    n2=len(b)
    if(a[0]==b[0]):
        print("The lists have same first element")
    if(a[n1-1]==b[n2-1]):
        print("The lists have same last elements")

listelements(l1)
listelements(l2)
listelements(l3)
listcomparision(l1,l2)
listcomparision(l1,l3)
listcomparision(l2,l3)
