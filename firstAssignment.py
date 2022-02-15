CODEWORD = 'SONAR'
CODE_ARR = list(CODEWORD)

def input_check(user_input):
    return user_input.lower() == CODEWORD.lower()

def get_spot_details(spot_val):
    if spot_val:
        if spot_val == 'NA':
            return 'Not in any spot'

        return 'Correct spot'

    return 'Incorrect spot'


def spell_check(user_input):
    arr = list(user_input)
    result = []
    for i in range(len(CODEWORD)):
        char = arr[i].upper()
        if char not in CODE_ARR:
            result.append('NA')
            continue
        if char != CODE_ARR[i]:
            result.append(False)
            continue
        result.append(True)

    for i in range(len(CODEWORD)):
        decider = result[i]
        user_char = user_input[i]

        print('%s --> %s'%(user_char, get_spot_details(decider)))

def main():
    count = 0
    while count < 6:
        user_input = input('Enter a word: ')
        if len(user_input) != 5:
            print('Please enter a 5-letter word!')
            continue
        if input_check(user_input):
            print('Matched')
            break

        spell_check(user_input)
        count += 1

if __name__ == "__main__":
    main()