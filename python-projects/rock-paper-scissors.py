# lets users play 2-player rock-paper-scissors
# teaching points:
  # infinite game loops and breaking statements

def compare(u1, u2): # tests and returns results of rock paper scissors
  if u1 == u2:
    print("It's a tie!")
  elif u1 == 'rock': # accounts for all possible results
    if u2 == 'scissors':
      print("{} won because {} ROCKs!".format(user1, user1))
    else:
      print("{} won with paper!".format(user2))
      
  elif u1 == 'scissors':
    if u2 == 'paper':
      print("{} won with scissors!".format(user1))
    else:
      print("{} won because {} ROCKs!".format(user2, user2))
  
  elif u1 == 'paper':
    if u2 == 'rock':
      print("{} won with paper!".format(user1))
    else:
      print("{} won with scisors!".format(user2))
  else: # rejects all other responses
    print("Hey! Choose rock, paper or scissors!")
    

def game():
  while True: # creates game loop to be quit with 'n'
    
    # asks users for rock/paper/scissors
    user1_choice = input("\n{}, do you choose rock, paper or scissors? ".format(user1)).lower()
    user2_choice = input("{}, do you choose rock, paper or scissors? ".format(user2)).lower()
    
    compare(user1_choice, user2_choice)
    # asks user if they want to play again
    
    play_again = input("Do you want to play again? Y/n").lower()
    if play_again == 'n':
      print("Okay, bye!")
      break
    

# asks users for name
print("Welcome to rock-paper-scissors for the irrationally lazy!")
user1 = input("What's your name? ")
user2 = input("And your name? ")

game()
