# functions used
def print_list():
    # print out the list
    count = 0
    for item in my_list:
        count += 1
        print(str(count) + '.', end = ' ')
        print(item)


def print_final_list():
    # print out list
    print_list()
    count = 0

    file_name = "list.txt"
    file = open(file_name, "a")
    for item in my_list:
        count += 1
        file.write(str(count) + '. ' + item + '\n')
    file.close()


def help_me():
    # print out instructions on how to use the app
    print("What do we want to do today?")
    print("Type 'DONE' to stop keying in items.")
    print("Type 'SHOW' to see current list.")
    print("Type 'HELP' to see the list of commands available.")


def add_item():
    while True:
        # ask for new items
        new_item = input("> ")

        # quit the app
        if new_item.lower() == 'done':
            break
        # show the current list under 'SHOW'
        elif new_item.lower() == 'show':
            print_list()
            continue
        # show the help menu
        elif new_item.lower() == 'help':
            help_me()
            continue

        else:
            # add new items to our list
            my_list.append(new_item)
            print("{} now added to list. {} item(s) in list currently.".format(new_item, len(my_list)))


# make a list that holds our items
my_list = []

# actual actions
help_me()

add_item()

print_final_list()
