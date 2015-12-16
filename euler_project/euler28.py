result = 1
for i in range(2, 1002):
	if i%2:
		result += pow(i,2)
	else:
		result += 3*pow(i,2)+3

print result
