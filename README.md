Hangman Game in Python
This is a simple command-line Hangman game implemented in Python. The game randomly selects a word from a predefined list, and the player must guess the word one letter at a time before they run out of allowed incorrect guesses.

📋 Features
Random word selection from a list
Tracks guessed letters
Displays current progress of the word
Allows a maximum of 6 incorrect guesses
Input validation and duplicate guess handling

🛠️ How It Works
A word is randomly chosen from a predefined list.
The player is prompted to enter a letter guess.
If the guess is correct, the corresponding positions in the word are revealed.
If the guess is incorrect, the number of remaining tries decreases.
The game ends when the word is completely guessed or the player runs out of guesses.

🚀 Getting Started
Prerequisites
Python 3.x

Running the Game
Save the code in a file, for example Hangman game.py.
Open a terminal or command prompt.
Run the game using:
Hangman game.py

Output Example
=== Welcome to Hangman ===
Guess the word one letter at a time.
You have 6 incorrect guesses allowed.

Word: _ _ _ _ _
Guessed letters: 
Enter a letter: a
 Correct!

Word: _ a _ _ _
Guessed letters: a
Enter a letter: z
 Wrong! You have 5 tries left.

 📄 Code Structure
secret_word: randomly chosen word from the list
display_word: visual representation of the word with unguessed letters as _
guessed_letters: list of letters already guessed
incorrect_guesses: tracks how many wrong attempts have been made
max_incorrect: maximum allowed incorrect guesses (set to 6)
