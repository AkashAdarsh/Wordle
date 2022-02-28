import random


def get_random_word():
    check_if_all_words_have_been_used()
    with open('valid_words.txt', 'r+') as file_pointer:
        content = file_pointer.read().split('\n')
        content = [i for i in content if i]
        random_word = content[random.randint(0, len(content) - 1)]
        word = random_word if len(random_word) > 0 and len(random_word) == 5 and \
              not check_if_word_exists('used_words.txt', random_word) else get_random_word()
        file_pointer.close()
        return word


def check_if_all_words_have_been_used():
    valid_words_count = sum(1 for _ in open('valid_words.txt'))
    used_words_count = sum(1 for _ in open('used_words.txt'))
    if valid_words_count == used_words_count:
        open('used_words.txt', 'w').close()


def check_if_word_exists(filename, word):
    with open(filename, 'r+') as file_pointer:
        content = file_pointer.read().split('\n')
        is_word_present = word in content
        file_pointer.close()
        return is_word_present


def add_word_to_used_list(word):
    with open('used_words.txt', 'a+') as file_pointer:
        file_pointer.write(str(word) + '\n')
        file_pointer.close()
