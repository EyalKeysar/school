import enchant
import sys

d = enchant.Dict("en_USs")

def get_words(filename):
    try:
        txt = open(filename, "r").read()
        words = txt.split()
        words.sort()
        return words
    except FileNotFoundError:
        print("File not find")
        return []
    
def add_word_to_dict(word_count, word):
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

def main():
    
    print(get_words("alice.txt"))
if(__name__ == "__main__"):
    main()