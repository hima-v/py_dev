#Program for formatting word 
def slice_fn(word,n):
    a= (word[:n]) #characters after n will be skipped
    b= (word[n:]) #first n characters will be skipped
    print (a)
    print (b)
str1="its about drive its about power"
slice_fn(str1,4)
