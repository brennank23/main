# Katie Brennan, email kmb327@cornell.edu
# Python personal project, user-interactive application utilizing random library
# to be continuously edited, improved, expanded, and tested.
# 12/01/2019
# https://katiebrennan.github.io

import random #python random library
from random import shuffle #specific random pkg for shuffling a list of integers

# mainMenu() this is the main menu, where the user is presented with the options for random mini aps
# using a while loop allows us to run the main menu until the user decides to quit
def mainMenu():
    while True:
        # print menu items each time and get user selection
        print ('This is a random generator application.  You have several options:')
        print('1. Heads or Tails')
        print('2. Random Number from Range')
        print('3. Shuffle A List')
        print('4. Quit')
        selection = int(input("Enter choice: ")) # user input
        # compare to menu values and call corresponding functions
        if selection ==1:
            headsOrTails()
        elif selection==2:
            randomRange()
        elif selection == 3:
            shuffleList()
        elif selection == 4:
            print("Quitting...")
            return # exit entire program
        else:
            print("Enter a valid integer choice, 1-4.") # user choice invalid
        continue # send control back to top of while loop, main menu again

# heads or tails gives the user(s) an opportunity to simulate a coin flip using
# psuedorandom methods from the python library
# using a while loop allow to keep track of score as long as desired
def headsOrTails():
    print("In this game, select heads or tails and determine the result without an actual coin.")
    player1 = 0 # num wins
    computer = 0 #num wins
    play = True # boolean flag
    while play: # user wants to contine current game
        pSelect = str(input("Player, CALL THE TOSS! Enter H for Heads or T for Tails: "))
        if pSelect == 'H' or pSelect == 'h':
            cSelect = 'T'
        elif pSelect == 'T' or pSelect == 't':
            cSelect = 'H'
        print("Flipping coin...")
        flip = random.randint(0,1) # 0 is Heads 1 is Tails !!!
        if flip == 0: # flip is heads, 0
            print("Heads!")
            # player selected heads and wins
            if pSelect.lower() == 'h' or pSelect.lower() == 'heads' or pSelect.lower() == 'head':
                print("Player won!")
                player1+=1
            else: # pSelect == 'T', computer wins. increment appropriate local vars
                print("Computer won.")
                computer+=1
        else: # flip == 1, tails
            print("Tails!")
            # player selected tails and wins
            if pSelect.lower() == 't' or pSelect.lower() == 'tails' or pSelect.lower() == 'tail':
                print("Player won!")
                player1+=1
            else: # pselect is 'H', computer wins, increment local vars
                print("Computer won.")
                computer+=1
        print("SCORE: ") # score update
        print("Player: " , player1 , "    Computer: " , computer)
        # ask user if they want to continue playing
        again = str(input("Would you like to continue playing? Y/N: "))
        if again == 'Y' or again == 'y' or again == 'yes' or again == 'Yes':
            continue # continue with same score if yes
        else: # else reset players and set boolean flag to false
            player1 = 0
            computer = 0
            play = False
    return # return to main menu upon exiting while loop

# randomRange() this function allows the user to enter a range of integers and returns a random selection
# from that range using the pseudorandom function included with Python.
# using a while loop allows us to continue selecting random ints from same range as long as desired
def randomRange():
    same = True
    print("Choose a range of integers, and this will return a random integer in that range")
    begin = int(input("Enter an integer for your lower bound (inclusive): "))
    end = int(input("Enter an integer for your upper bound(inclusive): "))
    while same:
        # option for user to enter their guess before selection
        guess = str(input(("Would you like to enter a guess? Y/N: ")))
        if guess == 'Y' or guess == 'y':
            num = int(input("Enter your guess in range: "))
        else:
            # put variable out of possible range otherwise
            num = random.randint(end+5, end+6)
        print("Making random selection...")
        selection = random.randint(begin,end)
        if guess == 'Y' or guess == 'y':  # user did make a guess
            if num == selection:  # it was right, return it
                print("Woah! ", selection," is right!")
            else: # user guess was wrong
                print("Better luck next time. The random int was ", selection)
        else: # didn't make a guess, just return result
            print("The random integer from range [",begin,',',end,'] is ', selection)

        # ask user if they want to choose another rand int from same Range
        # set boolean flags accordingly
        again = str(input("Choose another random int from same range? Y/N: "))
        if again.lower() == 'y' or again.lower()=='yes':
            continue
        else:
            same = False
    return # return to main menu upon exiting while loop

# shuffle list utilizes Python's shuffle function from the random library
# it allows the user to enter a list of any type and number of elements
# then prints back out that list randomly shuffled according to its indices
# use of a while loop allows user to continually shuffle same list if desired
def shuffleList():
    print("Enter the list you want shuffled, letters or numbers, and this will give you a randomly shuffled version.")
    size = int(input("How many items in your list?: ")) #ask user for num items in list
    list = []
    # populate the list with the user desired elements
    for i in range(size):
        elem = str(input('Name/ID: '))
        list.append(elem)
    again = True
    while again:
        order = [] # another integer array to be used to store indices of OG list
        for i in range(size):
            order.append(i)
        print("SHUFFLING the LIST...")
        shuffle(order) # using Python random shuffle on int array of indices
        # printing out the list elements at the random order of indeices
        for j in range(size):
            print(list[order[j]])
        # ask user if they want to shuffle again and set boolean flag/continue
        again = str(input("Shuffle the same list again? Y/N: "))
        if again.lower() == 'y' or again.lower() == 'yes':
            continue # throw control back to beginning of while loop
        else:
            again = False
    return # if out of while loop return to main menu

# kick off entire process with call to main menu
mainMenu()
