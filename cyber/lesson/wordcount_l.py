import sys
import os
import enchant
ALICE_TEXT = 1


def count_words():
    complete_text = ''
    with open(sys.argv[ALICE_TEXT]) as lines:
        for line in lines:
            complete_text += line
    # print(complete_text)
    symbols = ['!', '_', '(', ')', '.', ',', '-', '*', ':', '\"', '?', '`']
    for symbol in symbols:
        complete_text = complete_text.replace(symbol, ' ')
        # if symbol == '\'s':
        #     complete_text.replace(symbol, '')
        # else:
        #     complete_text.replace(symbol, ' ')
    words = complete_text.split()
    eng_dict = enchant.Dict('en_US')
    alice_dict = {'names': 0, 'numbers': 0}
    for word in words:
        # if len(word) == 1:

        word = word.lower()
        if word.isdigit():
            alice_dict['numbers'] += 1
        elif eng_dict.check(word):
            if word in alice_dict:
                alice_dict[word] += 1
            else:
                alice_dict.update({word: 1})
        else:
            print(word)
            alice_dict['names'] += 1
    return alice_dict


def parameters_exist():
    if len(sys.argv) >= 1:
        if os.path.exists(sys.argv[ALICE_TEXT]):
            return True
        else:
            return False
    else:
        return False


def main():
    # count_words()

    alice_dict = {}
    if parameters_exist():
        alice_dict = count_words()
    else:
        print('NO PARAMS')
    for key, value in alice_dict.items():
        print(key, value)

    # word_check = '12345'
    # print(word_check[-2], word_check[-1])
    # eng_dict = enchant.Dict('en_US')
    # if eng_dict.check(word_check):
    #     print('exists')
    # my_dict = {}
    # word = 'lalala'
    # my_dict.update({word: 0})
    # word = 'blabla'
    # my_dict.update({word: 0})
    # print(my_dict)


if __name__ == '__main__':
    main()