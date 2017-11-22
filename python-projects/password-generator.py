import random

# utilises random.choice
# morphs big words into indecipherable passwords with random numbers and upper and lower cases if strong password. Weak: picks word from list

word_list = [
    "abnegation",
    "baseline",
    "adumbrate",
    "agrundize",
    "contusion",
    "exacerbate",
    "insidious",
    "pellucid",
    "zealous",
    "indecipherable",
    "unbelievable",
    "incoherent",
    "otherbigwords",
    "lmaoyoullneverguessthis",
    "justasmalltowngirl",
    "living in a lonely world"
    ]

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()?"

def truly_random_gen():  # generates password of passlen with no duplicate characters
	actual_random_word = "".join(random.sample(letters,strong_pass_length))
	print(actual_random_word)

def strong_random_gen():
	base_word = list(random.choice(word_list))
	new_word = []
	for letter in base_word:
		in_word = random.randrange(0,2)
		if in_word == 1:  # randomly adds some letters to password
			to_upper = random.randrange(0,2)
			if to_upper == 1:  # randomly makes some letters upper
				new_word.append(letter.upper())
			elif to_upper == 0:
				new_word.append(letter.lower())
		else:
			randnum = random.randrange(0,10)
			add_number = random.randrange(0,2)  # randomly adds some numbers
			if add_number == 1: 
				new_word.append(str(randnum))
	print(''.join(new_word))

def weak_random_gen():
	new_word = random.choice(word_list)
	print(new_word)
  

  
while True:  # allows user to request for password (loop till 'n')
	pass_request = input("Generate a password? Y/n > ").lower()
	if pass_request != 'n':
		weak_strong = input("Do you want password to be weak or STRONG? > ").lower()
		if weak_strong == 'weak':
			weak_random_gen()
		else:
			strong_random_gen()
	if pass_request == 'n':
		print("Ok, bye!")
		break
    
while True:
	strong_pass_request = input("Generate a truly random password? Y/n > ").lower()
	if strong_pass_request != 'n':
		strong_pass_length = int(input("How many characters do you want? > "))
		truly_random_gen()
	else:
		print("Ok, your loss!")
		break
