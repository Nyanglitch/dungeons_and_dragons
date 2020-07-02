import random

print("Welcome to DUNGEONS AND DRAGONS")
print("You see two caves in front of you.\nOne has treasures, other - certain death!")

random_death_phrases = ["fire breath!", "lunar dragon magic!", "pit with sharp sticks!", "shark-dragon!", "deadly gas!", "falling and breaking your neck!"]

counter = 0
gold = 0
gold_looted = 0
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
		counter += 1
		gold_looted = random.randint(0, 666)
		gold += gold_looted
		print("Lucky! Gold looted:", gold_looted)
	else:
		if gold >= 500:
			death_insurance = input("You are about to die!\nWould you like to prevent this for 500 gold? (y/n): ").lower()
			if death_insurance == "y":
				gold -= 500
				continue
		print("You died from " + random_death_phrases[random.randrange(0, len(random_death_phrases))] + "\nLucky caves:", counter, "\nGold you looted and lost:", gold)
		continue_input = input("Play again? (y/n): ").lower()
		counter = 0
		gold = 0
		while continue_input not in allowed_continue_inputs:
			continue_input = input("Letter not supported. Play again? (y/n): ").lower()