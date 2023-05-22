# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

## Creating the variables for the game
We have created a word_list variable conisisting of five fruit names. 

Then we have imported a random choice module to pass the word_list variable into the choice method which later randomly generates a word from that list on to the word variable.

User then gets to input a guess of a random letter with the input variable and this becomes the guess variable.

Their guess is later verified to be a character with the if-else statement.

## Checking if the guessed character is in the word
We have iteratively checked whether the guess by the user was valid with the while loop function involving further if-else statements to check if the guessed letter is in the random word from the word_list. 

Functions were later created to check the guessed letter and to then ask for the input from the user. 

