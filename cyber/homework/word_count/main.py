import os

main_dir = r"C:\Networks\school\cyber\homework\word_count"
INPUT_PATH = main_dir + r"\input.txt"
DICT_PATH = main_dir + r"\words.txt"
OUTPUT_PATH = main_dir + r"\output.txt"

file = open(INPUT_PATH, "r")
words = file.read().split(" ") # Read file and split its words

dictionary = open(DICT_PATH, "r")
valid_words = dictionary.read().split("\n")

def get_word():
    """
    This function takes input from the user and returns it.

    Returns:
        String: The word taken from user.
    """

    return input("word : ")

def validate_word_list(words):
    return [word for word in words if word in valid_words]

def write(correct_words):
    f = open(OUTPUT_PATH, "w")
    f.write("\n".join(correct_words))