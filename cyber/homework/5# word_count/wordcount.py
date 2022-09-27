# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

# Imports
import sys
import enchant
import english_words

TEXT_FILE_NAME = "alice.txt"
EN_DICT_WORDS = english_words.english_words_set  # List of words that are in the English dictionary
EN_ALPHA_WORDS = english_words.english_words_lower_alpha_set
enchant_dict = enchant.Dict("en_US")
enchant_dict_uk = enchant.Dict("en_UK")
word_count = {}

def word_in_lib_check(word: str) -> bool:
    return word in english_words.english_words_lower_alpha_set or word in english_words.english_words_alpha_set or word in english_words.english_words_set or word in english_words.english_words_lower_set or enchant_dict.check(word) or enchant_dict_uk.check(word)

def add_word_to_dict(word_count, word):
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

def get_words(file_name: str) -> list[str]:
    try:
        txt = open(file_name, "r").read()
        words = txt.split()
        return words
    except FileNotFoundError:
        print("File not found")
        sys.exit(1)

def strip_word(word: str) -> str:
    symbols = ['!', '_', '(', ')', '.', ',', '-', '*', ':', '\"', '?', '`', "'", ";", "[", "]"]
    new_word = word
    for symbol in symbols:
        new_word = new_word.replace(symbol, "")
    return new_word

def sub_words(words: list, word_count: dict, unsubbed_words: list) -> None:
    for word in words:
        # Checks if word contains 2 word inside
        for i in range(len(word)):
            first = word[:i]
            second = word[i:]
            if(word_in_lib_check(first) and word_in_lib_check(second)):
                add_word_to_dict(first, word_count)
                add_word_to_dict(second, word_count)
                break

        # Checks if word contain another word.
        for i in range(len(word)):
            longest_len = 0
            longest_word = ""
            first = word[:i]
            if(word_in_lib_check(first)):
                if(len(first) > longest_len):
                    longest_len = len(first)
                    longest_word = first
        add_word_to_dict(first, word_count)
        
            



def add_words(words: list, word_count: dict, bad_words: list) -> None:
    for word in words:
        saved_word = word
        word = word.lower()

        if word_in_lib_check(word):
            # Normal word.
            add_word_to_dict(word_count, word)
        else:
            # If word has symboles in it.
            try:
                word = strip_word(word)
                if word_in_lib_check(word):
                    add_word_to_dict(word_count, word)
                else:
                    # If the current word start with an uppercase letter and is not in the dictionary so it is a name.
                    try:
                        if strip_word(saved_word)[0].isupper():
                            add_word_to_dict(word_count, strip_word(saved_word))
                        else:
                            print(word)
                            add_word_to_dict(bad_words, word)
                    except IndexError:
                        print("err: empty string")
            except ValueError:
                print("err: empty string (enchant)")
            



# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
    """
    """
    words_count = {}
    unnormal_words = {}
    words = get_words(TEXT_FILE_NAME)
    add_words(words, words_count, unnormal_words)
    print(unnormal_words)

def print_words(file_name: str) -> None:
    print("non def")

def print_top(file_name: str) -> None:
    print(file_name)

if __name__ == '__main__':
    main()
