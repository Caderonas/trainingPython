def sumOfMultiple(number):
	count = 0
	for i in range(1,number):
		if number%i == 0:
			count += i
	return count