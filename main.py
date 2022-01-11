import random

number = random.randint(0,10)
guess=12

while number!=guess:
  guess=int(input("Guess a number 0-10: "))
  if guess == number:
    print("You got it, nice job!")
  else:
    print("nope, guess again")

def makeFunction():
  print("test stuff")