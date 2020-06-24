import random

print("Welcome to DUNGEONS AND DRAGONS")
print("You see two caves in front of you.\nOne has treasures, other - certain death!")

counter = 0

def pick_destiny(counter):

	user_input = 0

	while int(user_input) not in [1, 2]:
		print("Which cave you'll pick? (1/2): ")
		user_input = input("> ")

	lucky_cave = random.randint(1, 2)

	if int(user_input) == lucky_cave:
		print("Lucky!")
		counter = counter + 1
		pick_destiny(counter)
	else:
		print("You died! Lucky caves: ", counter)

pick_destiny(counter)