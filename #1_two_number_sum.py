def twoNumberSum(array, targetSum):
    # Write your code here.
	#i = 0 # intiatilize the i
	for i in range(len(array)-1):
		j = i+1 # incremented the j value
		for j in range(i+1, len(array)):
			if array[i] +array[j]  == targetSum:
				return  array[i], array[j]
	return []

# we are using two for loop so complexity is o(n2) for time and
# space o(1)as we are using only one space

## this is one type of the solution, 
''' 
We can solve this from binary search also. 
Divide the array into two

# we can use hashing table. save the  target - a[i] and index 
compare this next element in the hash table if you have it and return the index 
here you incraese the space complexity but reduce the for loop so it is an optimal solutions for this problem
'''