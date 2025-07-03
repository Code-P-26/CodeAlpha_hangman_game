import random

word_list = ["mango", "table", "flower", "phone", "watch"]

secret_word = random.choice(word_list)

guessed_letters = []          
display_word = ["_"] * len(secret_word) 
max_incorrect = 6
incorrect_guesses = 0

print("=== Welcome to Hangman ===")
print("Guess the word one letter at a time.")
print(f"You have {max_incorrect} incorrect guesses allowed.\n")

while incorrect_guesses < max_incorrect and "_" in display_word:
    print("Word:", " ".join(display_word))
    print("Guessed letters:", " ".join(guessed_letters))
    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabetical letter.\n")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print(" Correct!\n")
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display_word[i] = guess
    else:
        incorrect_guesses += 1
        print(f" Wrong! You have {max_incorrect - incorrect_guesses} tries left.\n")

if "_" not in display_word:
    print("Congratulations! You guessed the word:", secret_word)
else:
    print(" Game over! The word was:", secret_word)
