'''
#Coin Flip Simulation - Write some code that simulates flipping a single coin however many times the user decides.
# The code should record the outcomes and count the number of tails and heads.
'''

import random

def flip_coin():
	flip_results = []
	total_heads = 0
	total_tails = 0
	num_of_flips = int(input('How many times do you want to flip the coin? '))

	for num in range(num_of_flips):
		flip_results.append(random.randint(1,2))

		while True:
			if flip_results[-1] == 1:
				total_heads += 1
				break
			else:
				total_tails += 1
				break

	print('The order of the sides were (1 = heads and 2 = tails: ' +str(flip_results))
	print('There were '+ str(total_heads) + ' head(s) and ' + str(total_tails) + ' tail(s) after doing ' + str(num_of_flips) + ' flips')

flip_coin()
