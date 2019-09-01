num = int(input('What is the numeber? '))

for n in range(2,num):
	if num%n==0:
		print('Not prime')
		print('Lowest factor is ' + str(n))
		break
else:
	print('Prime')