n,k=map(int,input().split())
ar=list(map(int,input().split()))
q=list(map(int,input().split()))
# Iterative Binary Search Function
# It returns index of x in given array arr if present,
# else returns -1
def binary_search(arr, x):
	low = 0
	high = len(arr) - 1
	mid = 0

	while low <= high:

		mid = (high + low) // 2

		# If x is greater, ignore left half
		if arr[mid] < x:
			low = mid + 1

		# If x is smaller, ignore right half
		elif arr[mid] > x:
			high = mid - 1

		# means x is present at mid
		else:
			return mid

	# If we reach here, then the element was not present
	return -1


# Test array
arr = [ 2, 3, 4, 10, 40 ]
x = 10

# Function call
result = binary_search(arr, x)

if result != -1:
	print("Element is present at index", str(result))
else:
	print("Element is not present in array")

# def bs(query):
#     num=query
#     le=0
#     ri=n-1
#     mid=0
#     while ri>=le:
#         mid=(le+ri)//2
#         if num>ar[mid]:
#             le=mid-1
#         elif num<ar[mid]:
#             ri=mid+1
#         else:
#             return("YES")
#     return("NO")
# for qu in q:
#     print(bs(qu))               