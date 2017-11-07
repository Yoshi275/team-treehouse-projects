import random





# play again

def game():
    # generate a random number between 1 and 10
    secret_num = random.randint(1, 10)
    guesses = []
    
    # limit guesses
    while len(guesses) < 5:
        try:
            # test for input to be integer (safely make an int)
            # get a number guess from player
            guess = int(input("Guess a number from 1 to 10: "))
        except ValueError:
            print("Hey, that's is not a number!")
            
        else:
            # compare guess to secret number
            if guess == secret_num:
                # print hit
                print("You got it! My number was {}. You took {} guesses.".format(secret_num, len(guesses)+1))
                break
            elif guess < secret_num:
                # too high message
                print("Try a higher number.")
            elif guess > secret_num:
                # too low message
                print("Try a lower number.")
            guesses.append(guess)
    else:
        print("Nice try! My number is actually {}. You took {} guesses and still didn't get it.".format(secret_num, len(guesses)))
    play_again = input("Do you want to play again? Y/n ").lower()
    if play_again != 'n':
        game()
    else:
        print("Okay. Bye!")

game()
