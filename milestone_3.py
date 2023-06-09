import random

word_list = ["banana", "apple", "pomegranate", "blueberry", "rambutan"]
word = random.choice(word_list)

def check_guess(guess):
    guess = guess.lower()

    if any(guess in word for word in word_list):
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")    

def ask_for_input():
    while True: 
        guess = input("Guess a letter: ")

        if len(guess) == 1 and guess.isalpha():
            check_guess(guess)
            break
        else:
         print("Invalid letter. Please enter a single alphabetical character.")


ask_for_input()