secret_word = 'metempsychosis'
cap_secret_word = secret_word.upper()

def play_hangman():
    print('Hello. I am the hangman.')
    reveal_letters = ''
    for i in range(len(secret_word)):
        reveal_letters = reveal_letters + '0'
    print(f'I am thinking of a {len(secret_word)} letter word: ' + reveal_letters)
    l = list(reveal_letters)
    while '0' in l:
        guess = input('Pick a letter: ')
        for i in range(len(cap_secret_word)):
            if guess.upper() == cap_secret_word[i]:
                l[i] = cap_secret_word[i]
            else:
                continue
        print('Revealed letters: ' + ''.join(l))
    print('You guessed all the letters! My word was: ' + cap_secret_word)

play_hangman()