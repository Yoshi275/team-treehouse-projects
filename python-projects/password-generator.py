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

def strong_random_gen():
  base_word = list(random.choice(word_list))
  new_word = []
  for letter in base_word:
    in_word = random.randrange(0,2)
    if in_word == 1: # randomly adds some letters to password
      to_upper = random.randrange(0,2)
      if to_upper == 1: # randomly makes some letters upper
        new_word.append(letter.upper())
      elif to_upper == 0:
        new_word.append(letter.lower())
    else:
      randnum = random.randrange(0,10)
      add_number = random.randrange(0,2) # randomly adds some numbers
      if add_number == 1: 
        new_word.append(str(randnum))
  print(''.join(new_word))

def weak_random_gen():
  new_word = random.choice(word_list)
  print(new_word)
  

  
while True: # allows user to request for password (loop till 'n')
  pass_request = input("Generate a password? Y/n ").lower()
  weak_strong = input("Do you want password to be weak or STRONG?").lower()
  if pass_request != 'n':
    if weak_strong == 'weak':
      weak_random_gen()
    else:
      strong_random_gen()
  if pass_request == 'n':
    print("Ok, bye!")
    break
    