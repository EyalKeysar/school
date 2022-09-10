'''
Eyal Keysar
8.9.2022

Baby Pampers
'''
LAST_NUBER = 5


def main():
    '''
    This is the main function, it will print all numbers
    between 0 and a given number (in the specific case the
    number is 5) in steps of 0.1, all natural numbers will
    be printed without a "." character.
    Function does not get any parameters and
    does not return any value.
    '''
    for i in range(LAST_NUBER):
        print(i)  # Prints the value of i (i is a natural number).
        # This for loop will print all of the
        # non natural numbers betwwen i and i+1.
        for j in range(1, 10):
            print(str(i) + "." + str(j))
    print(LAST_NUBER)  # Prints last number (because it is a natural).


if __name__ == "__main__":
    main()
