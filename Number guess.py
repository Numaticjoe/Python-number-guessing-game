# Python testing simple app too see if i like it??
# Written in VS2019 Community 
# By Numaticjoe 2022 
# Fixed a bug that wouldnt print you guessed it! 31/3/22

import random 
n = random.randint (1, 10)
guess = int(input("Type a number between 1 and 10!"))
while n != "guess":
	print
	if guess < n:
		print ("You guessed too low!")
		guess = int(input("Type a number between 1 and 10:"))
	elif guess > n:
		print ("You guessed too high!")
		guess = int(input("Type a number between 1 and 10:"))

	else:
		print ("you guessed it!")
		break
		print