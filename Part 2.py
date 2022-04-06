test_word='apple'
#test_word2='orange'
user_input=''
#wins=0
#loses=0
#key=test_word
#words_used=set()
#def get_word():
#    return test_word2
#def valid_word(word):
#    if word in words_used:
#        valid_new_word=get_word()
#        valid_word(valid_new_word)
#    else:
#        valid_new_word=word
#    return valid_new_word
word_knowledge= list("-"*len(test_word))
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
            if user_guess==test_word:
                print("You correctly guessed the word!  Congratulations, you won!")
                game_in_progress=False
            else:
                guesses_remaining-=1
                if guesses_remaining>0:
                    print("That is incorrect.")
        else:
            if test_word.find(user_guess)==-1:
                guesses_remaining-=1
                if guesses_remaining>0:
                    print("That is incorrect.")
            else:
                for i in range(0,len(test_word)):
                    if test_word[i]==user_guess:
                        word_knowledge[i]=user_guess
                if "".join(word_knowledge)==test_word:
                    print("You found all the letters, you won.")
                    game_in_progress=False
    else:
        guesses_remaining-=1
        if guesses_remaining>0:
            print("That is incorrect (invalid guess)")
    if guesses_remaining==0:
        print("That is incorrect, and was your last guess.  I'm sorry, you lost.")
        game_in_progress=False
                




