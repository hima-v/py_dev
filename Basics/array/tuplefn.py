# this code will explore all the input, iteration and special functions to
# perform in a tuple.

#approach 1:
# tup=tuple(int(input("Enter values")))
# print(tup)

# this doesnt work because int object aint iterable. you must keeo it at the last.
# it cant check for every value in tuple and make it int

#approach 2:

# tup=tuple(input("Enter values"))
# print(tup)

#firstly you will get string data type values
#sceondly- it will treat the spaces also as the string
#output: ['1', ' ' , '3' ]

#approach 3:
a = tuple(int(x) for x in a.split(","))


