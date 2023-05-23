import random

class Hangman: 
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.list_of_guesses = []
        self.word = random.choice(word_list)
        self.word_guessed = ['' for _ in range(len(self.word))]
        self.num_letters = len(set(self.word))

    def check_guess(self, guess):
        guess = guess.lower()

        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = guess
                    print(self.word_guessed)
            self.num_letters -= 1
            print(self.num_letters)
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word. Try again.") 
            print(f"You have {self.num_lives} lives left")   
        
        
    def ask_for_input(self):
        
        guess = input("Guess a letter: ")

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid letter. Please enter a single alphabetical character.")
        elif guess in self.list_of_guesses:
            print("You already tried that letter!")
        else:
            self.check_guess(guess)
            self.list_of_guesses.append(guess)

def play_game(word_list):
    game = Hangman(word_list, num_lives = 5)

    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        elif game.num_lives > 0 and game.num_letters == 0:
            print("Congratulations. You won the game!")    
            break
        

if __name__ == '__main__':       
    hangman = ["banana", "apple", "pomegranate", "blueberry", "rambutan"]
    play_game(hangman)



