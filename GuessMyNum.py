
"""
Guess The Number Game
"""
import random

compnum = random.randint(1, 100)
print(compnum)
print("In this game, you will have to guess the number that the computer has choosen from 1 to 100. What is your guess?")
guessNum = 0
listofguesses = []
a = "What's your next guess?"

while guessNum == 0:
  guessNum = guessNum + 1
  usernum = int(input())
  listofguesses.append(usernum)
  if compnum == usernum:
    print("Congrats! That's the number. It took you " + str(guessNum) + " attempt(s)")
    break
  elif usernum < 1 or usernum > 100:
    print("OUT OF BOUNDS " + a)
    break
  elif abs(compnum - usernum) > 10:
    print("COLD " + a)
    break
  else:
    print("WARM " + a)
    break

while True:
  guessNum = guessNum + 1
  usernum = int(input())
  listofguesses.append(usernum)
  if compnum == usernum:
    print("Congrats! That's the number. It took you " + str(guessNum) + " attempt(s)")
    break
  elif usernum < 1 or usernum > 100:
    print("OUT OF BOUNDS " + a)
  elif abs(compnum - usernum) <= abs(compnum - int(listofguesses[-2])):
    print("WARMER " + a)
  else:
    print("COLDER " + a)




    
































#a = int(random.randint(0,100))
#guessNum = 0

#while guessNum < 7:
 # print("What's your guess?")
  #guess = int(input())

#  guessNum = guessNum + 1
  
 # if a>guess:
  #  print("Too low")
  #elif a<guess:
   # print("Too high")
  #elif a == guess:
  #  print("Congrats")
 #   break
#print("Nice Try! Your number was " + str(a))
