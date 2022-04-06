import random

words_file=open(r"words_alpha(word list from gitHub).txt")
list_of_words=list(words_file.read().splitlines())
words_file.close()

test_word=random.choice(list_of_words)
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
    user_guess=guess_prompt()
    guesses_made[user_guess]=guess_count
    guess_count+=1
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
                for i in check_locations:
                    if test_word[i]==user_guess:
                        word_knowledge[i]=user_guess
                        known_locations.add(i)
                check_locations=check_locations-known_locations
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
print(f'The word was: {test_word}')
print(f'You made the following guesses: {guesses_made}')



