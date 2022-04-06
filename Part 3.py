key_word=""
words_file=open(r"words_alpha(word list from gitHub).txt")
list_of_words=list(words_file.read().splitlines())
print(list_of_words[1])
words_file.close()
word_knowledge= list("-"*len(key_word))
guesses_remaining=7
game_in_progress=True

while game_in_progress:
    print("".join(word_knowledge))
    print(f'You have {guesses_remaining} guesses remaining')
    user_guess=input('Enter a letter or word to guess (no numbers): ')
    valid_guess=user_guess.isalpha()
    if valid_guess:
        user_guess=user_guess.lower()
        if len(user_guess)!=1:
            if user_guess==key_word:
                print("You correctly guessed the word!  Congratulations, you won!")
                game_in_progress=False
            else:
                guesses_remaining-=1
                if guesses_remaining>0:
                    print("That is incorrect.")
        else:
            if key_word.find(user_guess)==-1:
                guesses_remaining-=1
                if guesses_remaining>0:
                    print("That is incorrect.")
            else:
                for i in range(0,len(key_word)):
                    if key_word[i]==user_guess:
                        word_knowledge[i]=user_guess
                if "".join(word_knowledge)==key_word:
                    print("You found all the letters, you won.")
                    game_in_progress=False
    else:
        guesses_remaining-=1
        if guesses_remaining>0:
            print("That is incorrect (invalid guess)")
    if guesses_remaining==0:
        print("That is incorrect, and was your last guess.  I'm sorry, you lost.")
        game_in_progress=False
print(f'The word was: {key_word}')




