def count_even(l):
	count = 0
	for num in l:
		if (not(num%2)):
			count+=1
	return count

print(count_even([1, 2, 3, 4, 5]))