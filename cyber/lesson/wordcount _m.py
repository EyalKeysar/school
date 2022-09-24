#!/usr/bin/python -tt
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
import enchant
import sys

d = enchant.Dict("en_UK")
# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.


def get_words(filename):
    try:
        txt = open(filename, "r").read()
        words = txt.split()
        words.sort()
        return words
    except FileNotFoundError:
        print("File not find")
        return []

def add_to_dict(word_count, word):
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1


def norm_words(words):
    word_count = {}
    bad_words = []
    for word in words:
        word = word.upper()
        if d.check(word) and word[len(word) - 1].isalpha():
            add_to_dict(word_count,word)
        else:
            bad_words.append(word)
    return word_count, bad_words


def alpha(word_count, bad_words):
    badder_words = []
    for word in bad_words:
        for char in word:
            if not char.isalpha():
                word = word.replace(char, "")
        if len(word) > 0:
            if d.check(word):
                add_to_dict(word_count, word)
            else:
                badder_words.append(word)
    return badder_words


def separate(word_count, bad_words):
    for word in bad_words:
        letters = list(word)
        leftovers = []
        while len(letters) > 0:
            if len(letters) > 0:
                if d.check("".join(letters)):
                    add_to_dict(word_count, "".join(letters))
                    letters = leftovers
                    leftovers = []
                else:
                    leftovers.insert(0, letters.pop())


def count_words(filename):
    words = get_words(filename)
    word_count, bad_words = norm_words(words)
    bad_words = alpha(word_count, bad_words)
    separate(word_count, bad_words)
    return word_count


def print_words(filename):
    print(count_words(filename))


def print_top(filename):
    word_count = count_words(filename)
    top_values = []
    for i in range(20):
        top_values.append(0);
    for key in word_count:
        for i in range(20):
            if word_count[key] > top_values[i]:
                top_values[i] = word_count[key]
                break
    for i in range(20):
        for key in word_count:
            if word_count[key] == top_values[i]:
                print(f"'{key}: {word_count[key]}'")
                word_count.pop(key)
                break

def main():
    if len(sys.argv) != 3:
        print("usage: ./wordcount.py {--count | --topcount} file")
        sys.exit(1)
    option =sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)

    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)
        sys.exit(1)


if __name__ == '__main__':
  main()
