import sys

no_of_tries = 5
word = "kamila"
used_letters = []
wants_to_play_again = "NIE"

user_word = []

def find_indexes(word, letter):
    indexes = []

    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)

    return indexes

def show_state_of_game():
    print()
    if user_word != []:
        print(user_word)
    print("Pozostało prób", no_of_tries)
    if used_letters != []:
        print("Użyte litery:", used_letters)
    print()

def appedning(word, user_word):
    for _ in word:
        user_word.append("_")

###

for _ in word:
    user_word.append("_")

while True:
    letter = input("Podaj literę: ")
    used_letters.append(letter)

    found_indexes = find_indexes(word, letter)

    if len(found_indexes) == 0:
        print("Nie ma takiej litery.")
        no_of_tries -= 1

        if no_of_tries == 0:
            print("Koniec gry :(")
            sys.exit(0)
    else:
        for index in found_indexes:
            user_word[index] = letter

        if "".join(user_word) == word:
            print("Brawo, to jest to słowo! :D")
            
            
            print("Czy chcesz zagrać ponownie?")
            print("TAK / NIE")
            print()
            wants_to_play_again = input()

            if wants_to_play_again != "TAK":
                sys.exit(0)
            else:
                no_of_tries = 5
                word = "kamila"
                used_letters = []
                user_word = []
                appedning(word, user_word)
            
    show_state_of_game()