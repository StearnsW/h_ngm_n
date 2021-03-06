test_word='apple' # word to test game with
word_knowledge= list("_"*len(test_word)) # what the player knows about the word

check_locations=set() # unknown letter locations
known_locations=set() # known letter locations
for i in range(0,len(test_word)): # initial letter location are all unknowns
    check_locations.add(i)

guesses_remaining=7 # guesses the player has left, initial value 7
game_in_progress=True # boolean to run the game loop, the player must play at least once, so begins as True
guess_count=1 # which guess is the player on
guesses_made={} # what guesses has the player made, in which order

# function prompting guesses, shows what the player already knows and how many guesses remaining, returns user input
def guess_prompt():
    print("".join(word_knowledge))
    print(f'You have {guesses_remaining} guesses remaining')
    guess=input('Enter a letter or word to guess (no numbers): ')
    return guess

while game_in_progress: # the game loop, runs until an end condition changes need to continue
    repeat_guess=False # boolean to see if guess has already been made, repeat guesses are incorrect
    user_guess=guess_prompt() # run the guess_prompt function and cast returned string as user_guess

    #check to see if user is repeating a guess, if so deducting a guess and telling the user it was a repeat
    if user_guess in guesses_made.values():
        repeat_guess=True
        guesses_remaining-=1
        print(f'You have already guessed that.')
    
    guesses_made[guess_count]=user_guess # records user's guess
    guess_count+=1 # increases guess counter in prep for next guess
    valid_guess=user_guess.isalpha() #check to see if the user guessed something alphabetic

    if valid_guess: # if alphabetic guess continue with game
        user_guess=user_guess.lower() # turn user input to lower case

        if len(user_guess)!=1: # check user inputted a word
            if user_guess!=test_word and not repeat_guess: # check if word is incorrect and not a repeat
                guesses_remaining-=1 # deduct from remaining guesses since wrong
                if guesses_remaining>0: # check if still have guesses left
                    print("That is incorrect.")
            elif not repeat_guess: # check if word not repeat
                print("You correctly guessed the word!  Congratulations, you won!")
                game_in_progress=False # since the user won, change need for game to continue to False
        else: # user inputted a single letter
            if test_word.find(user_guess)==-1 and not repeat_guess: # check if letter not in word and not repeat guess
                guesses_remaining-=1 # deduct from remaining guesses
                if guesses_remaining>0: # check if guesses remaining
                    print("That is incorrect.")
            else: # letter in word or repeat (repeat was dealt with and can't change so wastes RAM but easier read)
                for i in check_locations: # loop through the blank locations to see which need replacing
                    if test_word[i]==user_guess: # replace values where appropriate
                        word_knowledge[i]=user_guess
                        known_locations.add(i) # add changed locations to known locations

                check_locations=check_locations-known_locations # adjust blank locations for next iteration
                if "".join(word_knowledge)==test_word: # check if the player knows all the information to have won
                    print("You found all the letters, you won.")
                    game_in_progress=False # since the user knows all the letters, game need not continue
    
    elif not valid_guess and not repeat_guess: # if guess was invalid and not a repeat (repeats dealt with above)
        guesses_remaining-=1 # deduct from guesses remaining
        if guesses_remaining>0: # check if guesses remaining
            print("That is incorrect (invalid guess)")
    
    if guesses_remaining==0: # check if no guesses remain and game should end
        print("That is incorrect, and was your last guess.  I'm sorry, you lost.")
        game_in_progress=False # player has no more guesses so game should not continue

print(f'The word was {test_word}') # what was the word               
print(f'You made the following guesses: {guesses_made}') # all the player's guesses



