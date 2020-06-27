import random
import re

print("Welcome to DUNGEONS AND DRAGONS")
print("You see two caves in front of you.\nOne has treasures, other - certain death!")

counter = 0
continue_input = 'y'
user_input = ""
allowed_user_inputs = ['1', '2']
allowed_continue_inputs = ['y', 'n']

while continue_input == 'y':
	user_input = ''
	while user_input not in allowed_user_inputs:
		print("Which cave you'll pick? (1/2): ")
		user_input = input("> ")

	lucky_cave = str(random.randint(1, 2))

	if user_input == lucky_cave:
		print("Lucky!")
		counter = counter + 1
	else:
		print("You died! Lucky caves:", counter)
		continue_input = input("Play again? (y/n): ").lower()
		if continue_input not in allowed_continue_inputs:
			while continue_input not in allowed_continue_inputs:
				continue_input = input("Letter not supported. Play again? (y/n): ").lower()
		else:
			if continue_input == 'y':
				counter = 0
			else: 
				break