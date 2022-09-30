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
import math
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
    try:
        return enchant_dict_uk.check(word)
    #word in english_words.english_words_lower_alpha_set or word in english_words.english_words_alpha_set or word in english_words.english_words_set or word in english_words.english_words_lower_set or enchant_dict.check(word)
    except ValueError:
        print("err: checked empty word")
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
    symbols = ['!', '_', '(', ')', '.', ',', '-', '*', ':', '\"', '?', '`', "'", ";", "[", "]", "{","}"]
    new_word = word
    for symbol in symbols:
        new_word = new_word.replace(symbol, "")
    return new_word

def sub_words(words: dict, word_count: dict, unsubbed_words: dict) -> None:
    for word in words:
        if(len(word) > 2):
            word_exists = False;
            # Checks if word contains 2 word inside
            for i in range(len(word)):
                first = word[:i]
                second = word[i:]
                if(word_in_lib_check(first) and word_in_lib_check(second)):
                    word_exists = True
                    for i in range(words[word]):
                        add_word_to_dict(word_count, first)
                        add_word_to_dict(word_count, second)
                    break

        # Checks if word contain another word.
            for i in range(len(word)):
                first = word[:len(word) - i]
                if(word_in_lib_check(first)):
                    word_exists = True
                    for i in range(words[word]):
                        add_word_to_dict(word_count, first)
                    break
            if(not word_exists):
                for i in range(words[word]):
                    add_word_to_dict(unsubbed_words, word)
                
        
            



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
                            add_word_to_dict(bad_words, word)
                    except IndexError:
                        print("err: empty string")
            except ValueError:
                print("err: empty string (enchant)")
            
def get_min_dict(some_dict: dict):
    for key in some_dict:
        min = key
        break

    for key in some_dict:
        if(some_dict[key] < some_dict[min]):
            min = key
        
    return min

def print_most_used_words(word_count: dict) -> None:
    most_used = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0, "11": 0, "12": 0, "13": 0, "14": 0, "15": 0, "16": 0, "17": 0, "18": 0, "19": 0, "20": 0, "21": 0}
    for key in word_count:
        if(word_count[key] > most_used[get_min_dict(most_used)]):
            most_used[key] = most_used.pop(get_min_dict(most_used))
            most_used[key] = word_count[key]
    for key in most_used:
        print(key + "  :  " + str(most_used[key]))




# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
    # Setting up dictionaries.
    words_count = {}
    unnormal_words = {}
    
    # Get word list from text file.
    words = get_words(TEXT_FILE_NAME)
    
    # Adding words to dictionary.
    add_words(words, words_count, unnormal_words)
    # Checking for sub-words or two words connected.
    sub_words(unnormal_words, word_count, {})
    
    try:
        if(sys.argv[1] == "--top"):
            print_most_used_words(word_count)
        else:
            print(word_count)
    except IndexError:
        print("no argument (--count | --top)")
        for i in sys.argv:
            print(i)

if __name__ == '__main__':
    main()
