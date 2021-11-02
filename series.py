def series(str_number, n):
	for i in range(0, len(str_number)):
		if n == len(str_number[i:n+i]):
			print (str_number[i:n+i])
	return

series("49142", 3)