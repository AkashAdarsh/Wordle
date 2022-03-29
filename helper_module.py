def generate_possible_words(correct_letters, incorrect_letters):  # function for retrieving generating word
    with open('valid_words.txt', 'r+') as file_pointer:
        content = file_pointer.read().split('\n')
        file_pointer.close()
        words_list = [] #array for word list
        for word in content:    #loop for iterating through list
            count = 0
            letters = [str(i) for i in word]
            for letter in correct_letters:
                letter = letter.lower() #converting to lower case
                if letter in letters:
                    count += 1
            if count >= len(correct_letters):
                words_list.append(word)
        final_list = []
        for word in words_list:
            count = 0
            letters = [str(i) for i in word]
            for letter in incorrect_letters:
                letter = letter.lower()
                if letter in letters:
                    count += 1
            if count > 0:
                continue
            final_list.append(word)

        return final_list


def main():
    words_list = generate_possible_words(['A', 'B', 'C'], ['R']) #generrating words including a,b,c and excluding r
    print(words_list)


if _name_ == "_main_":
    main()