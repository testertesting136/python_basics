import random
words = ["cat", "monster", "fuzzy", "yarn"]

def select_word():
    return random.choice(words)

def display_word(secret_word, guessed_letters):
    displayed_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def main():
    secret_word = select_word()
    guessed_letters = []
    tries = 6

    while tries > 0:
        current_word = display_word(secret_word, guessed_letters)
        print(f"\nWord: {current_word}")
        print(f"Tries Remaining: {tries}")

        if current_word == secret_word:
            print("You won!")
            return
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in secret_word:
            guessed_letters.append(guess)
            print("Correct!")
        else:
            guessed_letters.append(guess)
            tries -= 1
            print("Incorrect!")
    print(f"You lost. The word was {secret_word}")
    
main()
