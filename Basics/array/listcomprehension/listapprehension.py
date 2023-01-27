#example 1: taking input and the input has many values, seperated by spaces 
arr = [int(x) for x in input().split()]
print(arr)
#example 2: list comprehension for initialising a boolean array
boolarr =  [True for i in range(6)]
print(boolarr)
print(type(boolarr))
print(boolarr[5])