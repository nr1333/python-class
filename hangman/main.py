
# HANGMAN GAME 







if __name__ == "__main__":
    word_length = input("What length word do you want to play with?: ")
    number_of_guesses = input("How many guesses would you like to have?: ")

    print(f"\nYou have {number_of_guesses} left.")
    print("Used letters: ")

    word = []
    word_length = int(word_length)
    for i in range(word_length):
        word.append('-')

    print(f"word {word}")

    #open dictionary for read ing and output all the contents 
    dictionary = open("dictionary.txt", "r")
    for i in range(5): 
        print(dictionary.readline())

    #open a certain line in dictionary file
    dictionary = open("dictionary.txt", "r")
    for i in range():
        print


