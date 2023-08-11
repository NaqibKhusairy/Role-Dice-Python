import random

while True:
	print("-------------------------------------")
	AskUser=input("Insert  Q tu quit or any key to Roll ")
	print("-------------------------------------")
	AskUser=AskUser.upper()
	if AskUser == 'Q':
		break
	else:
		number = random.randint(1, 6)
		print("You rolled: ", number)
