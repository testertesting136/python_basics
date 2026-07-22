import random
words = ["cat", "monster", "monster", "yarn"]

def main():
    word_choice = select_word()
    word_len = get_length(word_choice)
    tries = word_len
    print(f"Word contains: {word_len} letters")
    while tries > 0:
        user_guess = input("Guess the word: ")
        #print(is_game_over)
        split = split_word(word_choice)
        tries = game_over(split, user_guess, tries)

def select_word():
    random_word = random.choice(words)
    return random_word

def get_length(word):
    word_length = len(word)
    return word_length
    
def split_word(word):
    chars = []
    for i in word:
        chars.append(i)
    return chars

def game_over(split_word, input_word, tries):
    if input_word in split_word:
        tries -= 1
        print(f"tries: {tries}")
        return tries
    else:
        return tries
main()