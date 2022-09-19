import os
from spellchecker import SpellChecker


INPUT_PATH = r"C:\Networks\school\cyber\homework\word_count\input.txt"

file = open(INPUT_PATH, "r", encoding="utf8") # Open the file to read words from.
words = file.read().split(" ") # Read file and split its words

spell = SpellChecker()

def check(word):
    return word == spell.correction(word)

def main():
    count = 0
    if(os.path.isfile(INPUT_PATH) and os.path.splitext(INPUT_PATH)[1] == ".txt"):
        for word in words:
            if check(word):
                count += 1
        print(count)
    else:
        print("Error - input text file does not exists")

if __name__ == "__main__":
    main()
