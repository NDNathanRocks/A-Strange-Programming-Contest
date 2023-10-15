import random
import sys

with open('C:\Users\alice\AppData\Local\Temp\Temp5d3d7425-b7fa-47ad-83c5-d8d7475c0f2a_search.zip\proj1-search-python3\A-Strange-Programming-Contest\Problem5\words.txtt', 'r') as file:
    word_list = [word.strip() for word in file.readlines()]

num_words_to_guess, max_total_guesses = map(int, input().split())

def make_guess():
    return random.choice(word_list)

def flush_output():
    sys.stdout.flush()

def read_input():
    return input()

for _ in range(num_words_to_guess):
    remaining_guesses = max_total_guesses
    while remaining_guesses > 0:
        guess = make_guess()
        print(guess)  # Output the guess
        flush_output()  # Flush the output

        response = read_input()
        if response == "*****":
            break
        elif response == "ERROR":
            exit()

        remaining_guesses -= 1
exit()
