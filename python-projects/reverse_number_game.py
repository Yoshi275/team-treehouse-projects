import random

### Things to Improve ###
# ensure response is y/h/l
# allow for play again
# neaten up and refactor code
# let computer do smart guessing and pick between range based on data given, rather than lowest or highest being 1 or 10

def game():
    guesses = []
    # computer makes a random guess
    guess = random.randint(1,10)
    
    while len(guesses) == 1:
        
        # print guess for user
        print("Is the number {}? (Y)es/(H)igher/(L)ower ".format(guess))
        response = input("> ").lower()
        # tell computer if response is correct
        if response == 'y':
            print("Awesome! I took {} guesses and the number is ().".format(len(guesses), guess))
            break
        guesses.append(guess)
    
    while len(guesses) < 5:
        # print guess for user
        print("Is the number {}? (Y)es/(H)igher/(L)ower ".format(guess))
        response = input("> ").lower()
        # tell computer if response is correct
        if response == 'y':
            print("Awesome! I took {} guesses and the number is {}.".format(len(guesses)+1, guess))
            break
        # add guess to list
        guesses.append(guess)
        # tell computer to guess higher
        if response == 'h':
            print("Okay, so number is higher than {}.".format(guess))
            guess = random.randint(guess+1, 10)
        # tell computer to guess lower
        elif response == 'l':
            print("Okay, so number is lower than {}.".format(guess))
            guess = random.randint(1, guess-1)
    else:
        print("Shucks. I couldn't guess it in 5 guesses. You win!")
    
    #give user option to play again
    play_again = input("Play again? Y/n ").lower()
    if play_again == 'n':
        print("Okay, bye!")
    else:
        game()

game()