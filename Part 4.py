play_game=True
key_word=""
used_words=set()
wins=0
loses=0
import random

def guess_prompt():
    print("".join(word_knowledge))
    print(f'You have {guesses_remaining} guesses remaining')
    guess=input('Enter a letter or word to guess (no numbers): ')
    return guess

def get_word():
    words_file=open(r"words_alpha(word list from gitHub).txt")
    list_of_words=list(words_file.read().splitlines())
    words_file.close()
    word=random.choice(list_of_words)
    return word

while play_game:
    word_checked=False

    while not word_checked:
        test_word=get_word()
        if test_word not in used_words:
            word_checked=True
            key_word=test_word
            used_words.add(key_word)

    word_knowledge= list("-"*len(key_word))

    guesses_remaining=7
    game_in_progress=True
    guess_count=1
    guesses_made={}

    while game_in_progress:
        user_guess=guess_prompt()
        guesses_made[user_guess]=guess_count
        guess_count+=1
        valid_guess=user_guess.isalpha()
        if valid_guess:
            user_guess=user_guess.lower()
            if len(user_guess)!=1:
                if user_guess==key_word:
                    print("You correctly guessed the word!  Congratulations, you won!")
                    wins+=1
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
                        wins+=1
                        game_in_progress=False
        else:
            guesses_remaining-=1
            if guesses_remaining>0:
                print("That is incorrect (invalid guess)")
        if guesses_remaining==0:
            print("That is incorrect, and was your last guess.  I'm sorry, you lost.")
            loses+=1
            game_in_progress=False
    print(f'The word was: {key_word}')
    print(f'You made the following guesses: {guesses_made}')
    play_again=input("If you would like to play again type AGAIN, otherwise thanks for playing")
    if play_again!="AGAIN":
        play_game=False
print(f'You played {wins+loses} games with these words:{used_words}, earning {wins} wins and {loses} loses')




