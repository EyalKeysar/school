"""
Eyal Keysar
8.9.2022

Fibonacci
"""


def main():
    """
    This main function will print Fibonacci numbers until
    the next number will be bigger then 1000.
    """
    num1 = 0  # Default start numbers.
    num2 = 1
    while True:
        print(num1)
        # Adds 1st and 2nd numbers to the num2 and the 2nd number
        # will be the value of num1.
        temp = num1
        num1 = num2
        num2 += temp
        if num1 > 1000:
            break
        # The task requires the use of break.
        # Without the requirement I would use recursion.


if __name__ == "__main__":
    main()
