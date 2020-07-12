import random

list_of_words=[]
letters_guessed=[]
word=''
tries=0
guessed = False
guess=''
alphabet=''
status = ''

def play_again():
    global list_of_words
    global letters_guessed
    global word
    global tries
    global guessed
    global guess
    global alphabet
    global status

    list_of_words=[]
    letters_guessed=[]
    word=''
    tries=0
    guessed = False
    guess=''
    alphabet=''
    status = ''

    answer = input('Would you like to play again? yes/no').lower()
    if answer == 'y' or answer =='yes':
        words()
        displayCodedWord()
        # userInput()
        game()           
    else:
        print('Thank you and goodbye :)')
        pass

def words():
    global list_of_words
    list_of_words=['cat','dog','bear','frog','ostrich']

def getRandomWord():
    global list_of_words
    return random.choice(list_of_words)
    
def displayCodedWord():
    global alphabet
    global word
    global tries
    tries=6
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    word=getRandomWord()
    print('The word contains ', len(word), ' letters.')
    print(len(word) * '*')
    #print('You have ' + str(tries) + ' tries\n')

# def userInput():
#     global guess
#     guess = input('Please enter a letter or word.').lower()

def game():
    global guessed
    global alphabet
    global guess
    global tries
    global letters_guessed
    global word
    global status
     
    while guessed == False and tries > 0:
        print('You have ' + str(tries) + ' tries')
        guess = input('Please enter one letter or the full word.').lower()
        if len(guess) == 1:
            if guess not in alphabet:
                print('Enter a letter!')
            elif guess not in word:
                print('Its incorrectc :(')
                letters_guessed.append(guess)
                tries -=1
            elif guess in word:
                print('Correct!')
                letters_guessed.append(guess)
            else:
                print('Its incorrect :(')
        elif len(guess) == len(word):
            if guess == word:
                print('Well done,you have guessed it right!')
                guessed = True
            else:
                print('Its incorrect :(')
                tries -= 1
        else:
            print('The length of word you have entered is incorect!')
        
        status=''
        if guessed == False:
            for letter in word:
                if letter in letters_guessed:
                    status += letter
                else:
                    status += '*'
            print(status)

        if status == word:
            print('Brilliant,you have guessed the word!')
            guessed = True
        elif tries == 0:
            print('Oops you have run out guesses :(')  
    play_again()
    
    
words()
displayCodedWord()
# userInput()
game()        
