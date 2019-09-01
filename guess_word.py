import random
import time

def replay():
    return input("Do you want to play again? y/n? " ) == 'y'

def guess_word():
	word_bank = ['absorption', 'accompaniment', 'accomplice', 'acquiesce', 'acquittal', 'affiliation', 'benevolent', 'blasphemous',
		 'bravado', 'camouflage', 'capricious',  'chastise', 'chronic', 'citadel', 'clique', 'cocoon']
	print('In this game, you will need to guess the word. You will have a maximum of 8 incorrect guesses of letters.')
	start = input('Are you ready to play? y/n? ')
	
	faied_attempts = 8
	computer_word = random.choice(word_bank)
	print(computer_word)
	comp_word_letters = list(computer_word)
	print(comp_word_letters)

	empty_word = '_ '* len(comp_word_letters)


	while True:

		print('The word has ' + str(len(comp_word_letters)) + ' letters.')
		print(empty_word)
		time.sleep(0.5)
		user_guess = str(input('What letter is your guess? '))
		user_guess = user_guess.lower()
		if len(user_guess) != 1:
			print('Please guess one letter at a time')
		elif user_guess not in 'qwertyuiopasdfghjklzxcvbnm':
			print('Please guess only letters')

		if user_guess in comp_word_letters:
			print('Your guess was correct!')
			#NEXT STEP IS TO FIGURE OUT HOW TO REPLACE LETTERS AND CHECK GUESS
			#Find position of letter in word
			#Go back to list 
			#Find same index and replace blank with letter
			#Print list



		else:
			faied_attempts -= 1
			print('Incorret guess, you have ' + str(faied_attempts) + ' more.')
			if faied_attempts == 0:
				print('Sorry, game over.')
				if not replay():
					print('Thanks for playing')
					break
				else:
					continue
			else:
				continue

guess_word()