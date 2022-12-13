print("This program is to print the current number, previous number and their sum")
prev_num=0
for x in range(1,11):
    print("Current number is:", x, "Previous number is:", prev_num, "Sum is:", x+prev_num)
    prev_num=x