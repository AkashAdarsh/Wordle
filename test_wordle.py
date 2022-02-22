import unittest
import wordle
import dictionary
import user_interface
import statistics


class TestWordle(unittest.TestCase):

    def test_get_random_word(self):  # checking if its returning random word
        self.assertTrue(dictionary.get_random_word())

    def test_check_if_word_in_dictionary(self):  # checking if word exists in words.txt
        self.assertEqual(dictionary.check_if_word_in_dictionary('apple'), True)
        self.assertEqual(dictionary.check_if_word_in_dictionary('above'), True)
        self.assertEqual(dictionary.check_if_word_in_dictionary('mazda'), True)
        self.assertEqual(dictionary.check_if_word_in_dictionary('solve'), True)
        self.assertEqual(dictionary.check_if_word_in_dictionary('terry'), True)
        self.assertEqual(dictionary.check_if_word_in_dictionary('pigss'), False)

    def test_has_user_guessed_the_right_word(self):  # checking id the codeword and guessed word are right
        self.assertTrue(user_interface.has_user_guessed_the_right_word('apple', 'apple'))
        self.assertFalse(user_interface.has_user_guessed_the_right_word('soldo', 'anter'))
        self.assertTrue(user_interface.has_user_guessed_the_right_word('solve', 'solve'))
        self.assertFalse(user_interface.has_user_guessed_the_right_word('games', 'holys'))

    def test_check_if_entered_word_is_valid(self):  # checking if its a valid word
        self.assertEqual(user_interface.check_if_entered_word_is_valid('pipes'), True)
        self.assertEqual(user_interface.check_if_entered_word_is_valid('rail'), False)
        self.assertEqual(user_interface.check_if_entered_word_is_valid('saint'), True)
        self.assertEqual(user_interface.check_if_entered_word_is_valid('exist'), True)
        self.assertEqual(user_interface.check_if_entered_word_is_valid('uniform'), False)

    def test_get_input_from_user(self):  # checking id the output message for nth trial is right
        self.assertEqual(user_interface.get_input_from_user(1),
                         'hello')  # (please use only the words passed as arguments)
        self.assertEqual(user_interface.get_input_from_user(4),
                         'sonar')  # (please use only the words passed as arguments)

    def test_position_check_for_letters(self):  # checking if the position of each letter is matching
        self.assertEqual(user_interface.position_check_for_letters('sonar', 'solap'), [True, True, 'NA', True, 'NA'])
        self.assertEqual(user_interface.position_check_for_letters('exist', 'exits'), [True, True, True, False, False])
        self.assertEqual(user_interface.position_check_for_letters('fiber', 'fibre'), [True, True, True, False, False])
        self.assertEqual(user_interface.position_check_for_letters('genre', 'fonde'), ['NA', False, True, 'NA', True])
        self.assertEqual(user_interface.position_check_for_letters('party', 'hardy'), ['NA', True, True, 'NA', True])

    def test_check_if_word_in_dictionary(self):  # checking if word exists in words.txt
        self.assertTrue(dictionary.check_if_word_in_dictionary('apple'))
        self.assertTrue(dictionary.check_if_word_in_dictionary('above'))
        self.assertFalse(dictionary.check_if_word_in_dictionary('marza'))
        self.assertTrue(dictionary.check_if_word_in_dictionary('solve'))
        self.assertFalse(dictionary.check_if_word_in_dictionary('holys'))
        self.assertFalse(dictionary.check_if_word_in_dictionary('pigss'))

    def test_has_user_guessed_the_right_word(self):  # checking id the codeword and guessed word are right
        self.assertTrue(user_interface.has_user_guessed_the_right_word('harry', 'harry'))
        self.assertFalse(user_interface.has_user_guessed_the_right_word('anger', 'happy'))
        self.assertTrue(user_interface.has_user_guessed_the_right_word('green', 'green'))
        self.assertFalse(user_interface.has_user_guessed_the_right_word('hands', 'holys'))


if __name__ == '__main__':
    unittest.main()
