import random
HANGMAN_PICS = ['''
 +---+
     |
     |
     |
    ===''','''
 +---+
 O   |
     |
     |
    ===''','''
 +---+
 O   |
 |   |
     |
    ===''','''
 +---+
 O   |
/|   |
     |
    ===''','''
 +---+
 O   |
/|\  |
     |
    ===''','''
 +---+
 O   |
/|\  |
/    |
    ===''','''
 +---+
 O   |
/|\  |
/ \  |
    ===''','''
 +---+
[O   |
/|\  |
/ \  |
    ===''','''
 +---+
[O]  |
/|\  |
/ \  |
    ===''']

words = 'pizza burrito pie orange chips cake taco sandwich'.split()

#this function returns a random word from a list that you enter
def getRandomWord(wordList):
    randomIndex = random.randint(0, len(wordList)-1)
    return wordList[randomIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()
    print('missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=', ')
    print()
    blanks = '_' * len(secretWord)
#replace blanks with secret word   
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    #returns the letter the player guessed.  Makes sure the player entered a single letter and
    #not something else
    while True:
        print('Guess a letter...')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('You can only guess one letter at a time')
        elif guess in alreadyGuessed:
            print('You already guessed this.  Choose again')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('You can only guess letters.  Choose again')
        else:
            return guess

def playAgain():
    print('Do you want to play again? Yes or No?')
    return input().lower().startswith('y')
    
print('WELCOME TO HANGMAN!')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(missedLetters, correctLetters, secretWord)
    guess = getGuess(correctLetters + missedLetters)
    if guess in secretWord:
        correctLetters = correctLetters + guess
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print(secretWord + '! ' + 'You win!  Nice Job!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            print('You have run out of guesses! \nAfter ' + str(len(missedLetters)) + ' missed guesses, the word was ' + secretWord)
            gameIsDone = True

    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            secretWord = getRandomWord(words)
            gameIsDone = False
        else:
            break