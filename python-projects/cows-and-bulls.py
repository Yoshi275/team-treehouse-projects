import random


# function for checking numbers and adding cows and bulls
def compare_numbers(number, guess):
	cowbull = [0, 0]  # cow & bull count
	for i in range(len(number)):
		if number[i] == guess[i]:
			cowbull[0] += 1
		else:
			cowbull[1] += 1
	return cowbull


def cow_loop():
	# generate random number
	gen_num = str(random.randint(1000, 9999))

	# print welcome message
	print("Welcome to the Cows and Bulls game!")
	print("I have a number. Try guessing what it is. EXIT to quit game.")

	# allow user to enter guess
	print("For every correct number, you have a cow.")
	print("For every wrong number, you have a bull.")
	guess_count = []

	while len(guess_count) <= 50:
		guess = input("Enter a number: ")
		print(guess)
		if guess == gen_num:  # break loop if guessed correctly
			print("Bingo! The number is {}. You got it in {} guesses. Cow-ngratulations!".format(gen_num, len(guess_count)))
			break
		elif guess.lower() == 'exit':  # user quits game
			print("Thanks for playing!")
			break
		else:
			cowbull_count = compare_numbers(gen_num, guess)
			print("You have {} cows and {} bulls.".format(cowbull_count[0], cowbull_count[1]))
			guess_count.append(guess)

			if int(guess) < int(gen_num):  # clue on size of number
				print("Guess a larger number.")
			else:
				print("Guess a smaller number.")
	else:
		print("You have made too many mis-steaks. The number was {}. Try again next time.".format(gen_num))

	# option to repeat game
	if guess.lower() != 'exit':
		play_again = input("Do you want to play again? Y/n ").lower()
		if play_again != 'n':
			cow_loop()
		else:
			print("Nice playing. Bye!")


cow_loop()
