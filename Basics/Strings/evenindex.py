#print the even position characters
# issue 1- why the iteration is not moving ahead,, because i did x/2==0 (this compares quotient only)
# issue 2- it gets printed individually, but while creating list, its HIMA is out of range.

str1="cheempy"
str2="hima"
str3="nisarg"
a=list()
b=list()
c=list()
l1=len(str1)
l2=len(str2)
l3=len(str3)
l=max(l1,l2,l3)
for x in range(0,10):
    if (x%2==0):
        #while x<l1:
            a.append(str1[x])
        #while x<l2:
            b.append(str2[x])
        #while x<l3:
            c.append(str3[x])
        #print(str1[x], str2[x], str3[x])
    continue
print(a)
print(b)
print(c)
    
