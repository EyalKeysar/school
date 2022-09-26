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
import english_words


EN_DICT_WORDS = english_words.english_words_set  # List of words that are in the English dictionary
word_count = {}

def get_words(file_name: str) -> list[str]:
    try:
        txt = open(file_name, "r").read()
        words = txt.split()
        return words
    except FileNotFoundError:
        print("File not found")
        sys.exit(1)

def add_normal_words(words: list, word_count: dict, bad_words: dict) -> None:
    for word in words:
        if word in EN_DICT_WORDS:
            add_word_to_dict(word_count, word)
        else:
            add_word_to_dict(bad_words, word)

def add_word_to_dict(word_count, word):
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
    """
    """
    words = get_words(r"C:\Networks\school\cyber\homework\5# word_count\alice.txt")
    add_normal_words(words, {}, {})
    if len(sys.argv) != 3:
        print('usage: ./wordcount.py {--count | --topcount} file')
        sys.exit(1)
    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)
        sys.exit(1)


def print_words(file_name: str) -> None:
    """_summary_
    Args:
        file_name (str): _description_
    """
    print("non def")

def print_top(file_name: str) -> None:
    """_summary_

    Args:
        file_name (str): _description_
    """
    print(file_name)


if __name__ == '__main__':
    main()