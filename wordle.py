from user_interface import *
from dictionary import *


def main():
    codeword = get_random_word()
    trials = 6
    while trials > 0:
        user_word = get_input_from_user(trials)

        if not check_if_entered_word_is_valid(user_word):
            print('Please enter a 5-letter word!')
            continue

        if has_user_guessed_the_right_word(user_word, codeword):
            print('You guessed the right word!!!')
            break

        if check_if_word_in_dictionary(user_word):
            print('Warning! Please provide a valid dictionary word!')
            continue

        print('The word you entered -> %s' % user_word)
        user_word = user_word.lower()

        position_arr = position_check_for_letters(user_word, codeword)
        validate_letter_position(position_arr, user_word)
        trials -= 1

    print('Game over!!! Correct word was %s' % codeword)


if __name__ == "__main__":
    main()
