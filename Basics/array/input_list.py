#inputting the list by appending values to the list as per iteration count
t = int(input("Enter number of entries "))
n=[]
for i in range(t):
    el=int(input("Enter the number "))
    n.append(el)
print(n)
#next method of inputting is via map and split function
print("Next implemented code via map and split function")
l=input("Enter numbers with spaces ").split()
lc=list(map(int,l))
print(lc)