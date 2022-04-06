test_word='apple'
word_knowledge= list("_"*len(test_word))
check_locations=set()
known_locations=set()
for i in range(0,len(test_word)):
    check_locations.add(i)

guesses_remaining=7
game_in_progress=True
guess_count=1
guesses_made={}

def guess_prompt():
    print("".join(word_knowledge))
    print(f'You have {guesses_remaining} guesses remaining')
    guess=input('Enter a letter or word to guess (no numbers): ')
    return guess

while game_in_progress:
    repeat_guess=False
    user_guess=guess_prompt()
    if user_guess in guesses_made.values():
        repeat_guess=True
        guesses_remaining-=1
        print(f'You have already guessed that.')
    guesses_made[guess_count]=user_guess
    guess_count+=1
    valid_guess=user_guess.isalpha()
    if valid_guess:
        user_guess=user_guess.lower()
        if len(user_guess)!=1:
            if user_guess!=test_word and not repeat_guess:
                guesses_remaining-=1
                if guesses_remaining>0:
                    print("That is incorrect.")
            elif not repeat_guess:
                print("You correctly guessed the word!  Congratulations, you won!")
                game_in_progress=False
        else:
            if test_word.find(user_guess)==-1 and not repeat_guess:
                guesses_remaining-=1
                if guesses_remaining>0:
                    print("That is incorrect.")
            else:
                for i in check_locations:
                    if test_word[i]==user_guess:
                        word_knowledge[i]=user_guess
                        known_locations.add(i)
                check_locations=check_locations-known_locations
                if "".join(word_knowledge)==test_word:
                    print("You found all the letters, you won.")
                    game_in_progress=False
    elif not valid_guess and not repeat_guess:
        guesses_remaining-=1
        if guesses_remaining>0:
            print("That is incorrect (invalid guess)")
    if guesses_remaining==0:
        print("That is incorrect, and was your last guess.  I'm sorry, you lost.")
        game_in_progress=False
print(f'The word was {test_word}')                
print(f'You made the following guesses: {guesses_made}')



