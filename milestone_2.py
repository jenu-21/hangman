import random

word_list = ["banana", "apple", "pomegranate", "blueberry", "rambutan"]
print(word_list)    

word = random.choice(word_list)
print(word)

guess = input("Enter a single letter: ")
print("Your guess:", guess)

if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")
