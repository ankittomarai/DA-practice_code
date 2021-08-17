def getNthFib(n):
    # Write your code here.
	f = [0, 1]
	counter = 3
	while counter <= n:
		nextFib = f[0] + f[1]
		f[0] = f[1]
		f[1] = nextFib
		counter += 1
		
	return f[1] if n >1 else f[0]

## Here i have added solution for fibonacci series in python