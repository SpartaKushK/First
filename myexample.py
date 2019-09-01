
import random
a = int(random.randint(0,100))
guessNum = 0

while guessNum < 7:
  print("What's your guess?")
  guess = int(input())

  guessNum = guessNum + 1
  
  if a>guess:
    print("Too low")
  elif a<guess:
    print("Too high")
  elif a == guess:
    print("Congrats")
    break
print("Nice Try! Your number was " + str(a))