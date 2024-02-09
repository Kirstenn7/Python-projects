import random

print("Welcome to Hangman!")
print("-------------------")

from words import word

def get_valid_word(words):
    word = random.choice(words)  #randomly chooses a word from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word    

for x in word:
    print('_', end=' ')

def print_hangman(wrong):
    if(wrong == 0):
        print("\n+---+")
        print("    |")
        print("    |")
        print("    |")
        print("   ===")
    elif(wrong == 1):
        print("\n+---+")
        print("O   |")
        print("    |")
        print("    |")
        print("   ===")
    elif(wrong == 2):
        print("\n+---+")
        print("O   |")
        print("|   |")
        print("    |")
        print("   ===")
    elif(wrong == 3):
        print("\n+---+")
        print(" O  |")
        print("/|  |")
        print("    |")
        print("   ===")
    elif(wrong == 4):
        print("\n+---+")
        print(" O  |")
        print("/|\ |")
        print("    |")
        print("   ===")
    elif(wrong == 5):
        print("\n+---+")
        print(" O  |")
        print("/|\ |")
        print("/   |")
        print("   ===")
    elif(wrong == 6):
        print("\n+---+")
        print(" O  |")
        print("/|\ |")
        print("/ \ |")
        print("   ===")

def printWord(guessedLetters):
    counter=0
    rightLetters=0
    for char in word:
        if(char in guessedLetters):
            print(word[counter], end=' ')  #the end 'space' is so that we dont have new lines everytime
            rightLetters+=1
        else:
            print(' ', end=' ')
        counter+=1
    return rightLetters

def printLines():
    print('\r')  #printing a return character(this ensures that the lines show up underneath the guessed letters)
    for char in word:
        print('\u203E', end='')

#the following are variables for the while loop that makes the game work
length_of_word_to_guess = len(word)
amount_of_times_wrong = 0
current_guess_index = 0
current_letters_guessed = []
current_letters_right = 0

while(amount_of_times_wrong != 6 and current_letters_right != length_of_word_to_guess):  #!=  means not equal
    print('\nLetters guessed so far: ')  #here we dont have the end thing bc we want a new line
    for letter in current_letters_guessed:
        print(letter, end='')

    letterGuessed = input('\nGuess a letter: ')   #prompt the user for input
    #if user is right
    if(word[current_guess_index] == letterGuessed):
        print_hangman(amount_of_times_wrong)
        #print word
        current_guess_index+=1
        current_letters_guessed.append(letterGuessed)  #append adds the letters guessed
        current_letters_right = printWord(current_letters_guessed)
        printLines()
    #if user is wrong
    else:
        amount_of_times_wrong+=1
        current_letters_guessed.append(letterGuessed)
        #update the drawing
        print_hangman(amount_of_times_wrong)
        current_letters_right = printWord(current_letters_guessed)   #print word
        printLines()

print('Game Overrrrr') 