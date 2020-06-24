import random
import re

print("Welcome to DUNGEONS AND DRAGONS")
print("You see two caves in front of you.\nOne has treasures, other - certain death!")

counter = 0

def pick_destiny(counter):

	user_input = 0
	continue_input = 'u'

	while int(user_input) not in [1, 2]:
		print("Which cave you'll pick? (1/2): ")
		user_input = input("> ")

	lucky_cave = random.randint(1, 2)

	if int(user_input) == lucky_cave:
		print("Lucky!")
		counter = counter + 1
		pick_destiny(counter)
	else:
		print("You died! Lucky caves:", counter)
		while continue_input.lower() not in ['n', 'y']:
			continue_input = input("Play again? (y/n): ").lower()
		if continue_input == 'y':
			counter = 0
			pick_destiny(counter)

pick_destiny(counter)