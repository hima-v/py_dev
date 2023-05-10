## Created a function remove_min which eliminates the smallest number from the array
from inspect import getsource
def remove_min(a):
    arr=a
    n=len(a)
    j=0
    for i in range(1,n):
        if arr[i]<arr[j]:
            j=i
    arr.pop(j)
    return(arr)
print(remove_min([1,4,2,3]))
print(remove_min([5,4,2,3]))
print(__file__)
# help(pop)