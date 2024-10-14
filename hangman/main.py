
# HANGMAN GAME 







if __name__ == "__main__":
    word_length = input("What length word do you want to play with?: ")
    number_of_guesses = input("How many guesses would you like to have?: ")

    print(f"\nYou have {number_of_guesses} left.")
    print("Used letteers: ")

    word = []
    word_length = int(word_length)
    for i in range(word_length):
        word.append('-')

    print(f"word {word}")


