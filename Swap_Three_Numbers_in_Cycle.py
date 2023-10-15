# Python code addition 

def cyclic_swap(arr):
	# Before overwriting arr[1], store its value in temp.
	temp = arr[1]

	# Now do required swapping starting with arr[1].
	arr[1] = arr[0]
	arr[0] = arr[2]
	arr[2] = temp

a, b, c = 2, 4, 7
arr = [a, b, c]

print("Values before swapping:")
print("a =", arr[0], "\nb =", arr[1], "\nc =", arr[2])

cyclic_swap(arr)

print("Values after swapping:")
print("a =", arr[0], "\nb =", arr[1], "\nc =", arr[2])
