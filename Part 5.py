play_game=True # boolean for playing game, starts true, changes if player decides to not play again after finishing a game
key_word="" # the word being played in the game, different from test_word as it must be different each time
used_words=set() # set of played words, begins empty
wins=0 # counter for wins, begins at 0
loses=0 # counter for loses, begins at 0
import random # random to be used in finding word

# function which outputs a block or text to simulate gallows for the hanged man based on the guesses remaining
def gallows(gallows_int):
    if gallows_int==7: # empty gallows
        print("   ____ \n  |    |\n       |\n       |\n       |\n       |\n_______|\n")
    elif gallows_int==6: # add head
        print("   ____ \n  |    |\n  O    |\n       |\n       |\n       |\n_______|\n")
    elif gallows_int==5: # add sholders
        print("   ____ \n  |    |\n  O    |\n -+-   |\n       |\n       |\n_______|\n")
    elif gallows_int==4: # add torso
        print("   ____ \n  |    |\n  O    |\n -+-   |\n  |    |\n       |\n_______|\n")
    elif gallows_int==3: # add 1st arm
        print("   ____ \n  |    |\n  O    |\n -+-   |\n/ |    |\n       |\n_______|\n")
    elif gallows_int==2: # add 2nd arm
        print("   ____ \n  |    |\n  O    |\n -+-   |\n/ | \\  |\n       |\n_______|\n")
    elif gallows_int==1: # add 1st leg
        print("   ____ \n  |    |\n  O    |\n -+-   |\n/ | \\  |\n /     |\n_______|\n")
    else: # whole body (add 2nd leg)
        print("   ____ \n  |    |\n  O    |\n -+-   |\n/ | \\  |\n / \\   |\n_______|\n")

# function prompting guesses, shows what the player already knows and how many guesses remaining, returns user input
def guess_prompt():
    print("".join(word_knowledge))
    print(f'You have {guesses_remaining} guesses remaining')
    guess=input('Enter a letter or word to guess (no numbers): ')
    return guess

# function to get a word for each game instance, returns the randomly chosen word
def get_word():
    words_file=open("words_alpha(word list from gitHub).txt") # open list file to read in data
    list_of_words=list(words_file.read().splitlines()) # turn list file data into a list
    words_file.close() # close list file
    word=random.choice(list_of_words).lower() # chose a random word from the list
    return word

# loop to play multiple instances of the game
while play_game:
    word_checked=False # has the word chosen been checked, begins False as no word chosen for the game yet so can't have been checked

    # loop to check if is new word or not
    while not word_checked:
        test_word=get_word() # get a word

        if test_word not in used_words: # test if word is new
            word_checked=True # word is new so no need to recheck, change checked to True
            key_word=test_word # set key_word (the word to play) to the picked test_word
            used_words.add(key_word) # add the new word to play to the played words set

    word_knowledge= list("_"*len(key_word)) # what the player knows about the word
    check_locations=set() # unknown letter locations
    known_locations=set() # known letter locations
    for i in range(0,len(key_word)): # initial letter location are all unknowns
        check_locations.add(i)

    guesses_remaining=7 # guesses the player has left, initial value 7
    game_in_progress=True # boolean to run the game loop, the player must play at least once, so begins as True
    guess_count=1 # which guess is the player on
    guesses_made={} # what guesses has the player made, in which order

    while game_in_progress: # the game loop, runs until an end condition changes need to continue
        gallows(guesses_remaining) # show the players gallows progress
        repeat_guess=False # boolean to see if guess has already been made, repeat guesses are incorrect
        user_guess=guess_prompt() # run the guess_prompt function and cast returned string as user_guess

        #check to see if user is repeating a guess, if so deducting a guess and telling the user it was a repeat
        if user_guess in guesses_made.values():
            repeat_guess=True
            guesses_remaining-=1
            if guesses_remaining>0:
                print(f'You have already guessed that.')
    
        guesses_made[guess_count]=user_guess # records user's guess
        guess_count+=1 # increases guess counter in prep for next guess
        valid_guess=user_guess.isalpha() #check to see if the user guessed something alphabetic

        if valid_guess: # if alphabetic guess continue with game
            user_guess=user_guess.lower() # turn user input to lower case

            if len(user_guess)!=1: # check user inputted a word
                if user_guess!=key_word and not repeat_guess: # check if word is incorrect and not a repeat
                    guesses_remaining-=1 # deduct from remaining guesses since wrong
                    if guesses_remaining>0: # check if still have guesses left
                        print("That is incorrect.")
                elif not repeat_guess: # check if word not repeat
                    print("You correctly guessed the word!  Congratulations, you won!")
                    wins+=1 # add one to wins
                    game_in_progress=False # since the user won, change need for game to continue to False
            else: # user inputted a single letter
                if key_word.find(user_guess)==-1 and not repeat_guess: # check if letter not in word and not repeat guess
                    guesses_remaining-=1 # deduct from remaining guesses
                    if guesses_remaining>0: # check if guesses remaining
                        print("That is incorrect.")
                else: # letter in word or repeat (repeat was dealt with and can't change so wastes RAM but easier read)
                    for i in check_locations: # loop through the blank locations to see which need replacing
                        if key_word[i]==user_guess: # replace values where appropriate
                            word_knowledge[i]=user_guess
                            known_locations.add(i) # add changed locations to known locations

                    check_locations=check_locations-known_locations # adjust blank locations for next iteration
                    if "".join(word_knowledge)==key_word: # check if the player knows all the information to have won
                        print("You found all the letters, you won.")
                        wins+=1 # add one to wins
                        game_in_progress=False # since the user knows all the letters, game need not continue
    
        elif not valid_guess and not repeat_guess: # if guess was invalid and not a repeat (repeats dealt with above)
            guesses_remaining-=1 # deduct from guesses remaining
            if guesses_remaining>0: # check if guesses remaining
                print("That is incorrect (invalid guess)")
    
        if guesses_remaining==0: # check if no guesses remain and game should end
            print("That is incorrect, and was your last guess.  I'm sorry, you lost.")
            loses+=1 # add one to loses since the player lost
            game_in_progress=False # player has no more guesses so game should not continue
    print(f'The word was: {key_word}') # what was the word               
    print(f'You made the following guesses: {guesses_made}') # all the player's guesses
    play_again=input("If you would like to play again type AGAIN, otherwise thanks for playing  ") # prompt user to play again
    if play_again!="AGAIN": # if not AGAIN changes play boolean to False to stop playing
        play_game=False
print(f'You played {wins+loses} games with the words:{used_words}, earning {wins} wins and {loses} loses') # final game stats





