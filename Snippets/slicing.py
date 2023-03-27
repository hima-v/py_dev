#program for formatting a string/sentence
def slice_fn(word,n):
    a= word[:n] #characters after n will be skipped
    b= word[n:] #first n characters will be skipped
    print (a)
    print (b)
str1="PythonDev"
slice_fn(str1,6)
print(str1[::-1])
#list slicing:
l1=[2,4,6,12,16,18,22]
l=len(l1)
y=l1[0:l:2] #list[start:stop:step]
x=l1[::-1]  #reverse list
print(y)
print(x)

# OUTPUT:
# Python
# Dev
# [2, 6, 16, 22]
# [22, 18, 16, 12, 6, 4, 2]