from user_interface import *
from dictionary import *
from statistics import *
from logs import *


def main():
    codeword = get_random_word()
    add_word_to_used_list(codeword)
    log_to_file('info', 'The selected word is "%s"' % codeword)
    trials = 1
    while trials < 7:
        user_word = get_input_from_user(trials)
        log_to_file('info', 'Trial %s -> User input: "%s"' % (trials, user_word))

        if not check_if_entered_word_is_valid(user_word):
            print('Please enter a 5-letter word!')
            log_to_file('error', 'User entered invalid word')
            continue

        if has_user_guessed_the_right_word(user_word, codeword):
            print('You guessed the right word!!!')
            update_trial_upon_win(trials)
            log_to_file('info', 'User guessed the right word!!!')
            break

        if not check_if_word_exists('valid_words.txt', user_word):
            print('Warning! Please provide a valid dictionary word!')
            log_to_file('error', 'User entered invalid word')
            continue

        print('The word you entered -> %s' % user_word)
        user_word = user_word.lower()

        position_arr = position_check_for_letters(user_word, codeword)
        validate_letter_position(position_arr, user_word)
        trials += 1

    print('Game over!!! Correct word was %s' % codeword)
    total_games_played = increment_total_games_played()
    print("Total games played are - %s" % total_games_played)
    print('Win percentage: %s' % get_win_percentage())
    log_to_file('info', 'Win percentage: %s' % get_win_percentage())
    guess_distribution = get_guess_distribution()
    for i in range(len(guess_distribution)):
        print('%s -> %s' % (i + 1, guess_distribution[i]))
        log_to_file('info', 'Guess Distribution: Trial #%s -> %s' % (i + 1, guess_distribution[i]))


if __name__ == "__main__":
    main()
