l1=["Elements","of","list","are","joined","with","spaces"]
str1="hehe"
str2="hima"
print(' '.join(l1))
print("eee".join(str1)) #after every iterable, here character, the eee is added
print("x".join(i for i in str2 if (i=="a" or i=="i" )))



# OUTPUT:
# Elements of list are joined with spaces
# heeeeeeeheeee
# ixa