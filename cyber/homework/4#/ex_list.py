""" This program has been adapted for use by GVAHIM
       - the main revisions regard pep8 compliance and use of variable names

Copyright 2010 Google Inc.
Licensed under the Apache License, Version 2.0
http://www.apache.org/licenses/LICENSE-2.0

Google's Python Class
http://code.google.com/edu/languages/google-python-class/

Basic list exercises
Fill in the code for the functions below. main() is already set up
to call the functions with a few different inputs,
printing 'OK' when each function is correct.
The starter code for each function includes a 'return'
which is just a placeholder for your code.
It's ok if you do not complete all the functions, and there
are some additional functions to try in list2.py. """


# A. match_ends
# Given a list of strings, return the count of the number of
# strings where the string length is 2 or more and the first
# and last chars of the string are the same.
# Note: python does not have a ++ operator, but += works. HAVE FUN WITH PISTUN! @yuval was here
def match_ends(words):
    '''
    Given a list of strings, return the count of the number of
    strings where the string length is 2 or more and the first
    and last chars of the string are the same.
    '''
    return sum(len(i) > 1 and i[-1] == i[1] for i in words)

# B. front_x
# Given a list of strings, return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Hint: this can be done by making 2 lists and sorting each of them
# before combining them.
def front_x(words):
    """
    Given a list of strings, return a list with the strings
    in sorted order, except group all the strings that begin with 'x' first.
    """
    x_list = []
    not_x_list = []
    for i in words: # Adds to each list the words from words.
        if(i[0] == "x"):
            x_list.append(i)
        else:
            not_x_list.append(i)

    # Sorting the words lists.
    x_list.sort()
    not_x_list.sort()

    # Final result is the addition of the non x words to the x words.
    final_result = [i for i in x_list]
    for i in not_x_list:
        final_result.append(i)

    return final_result


# C. sort_last
# Given a list of non-empty tuples, return a list sorted in increasing
# order by the last element in each tuple.
# e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
# [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# Hint: use a custom key= function to extract the last element form each tuple.
def get_last_element(tup):
    """_summary_

    Args:
        tup (int): current tuple

    Returns:
        int: last element of the tuple
    """
    return tup[-1]

def sort_last(tuples):
    """
    Given a list of non-empty tuples, return a list sorted in increasing
    order by the last element in each tuple.
    """
    tuples.sort(key=get_last_element)
    return tuples

# D. Given a list of numbers, return a list where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
# modify the passed in list.
def remove_adjacent(nums):
    """
    Given a list of numbers, return a list where
    all adjacent == elements have been reduced to a single element.
    """
    if(len(nums) >= 1):
        new_list = [nums[0]]
        for i in nums:
            if(i != new_list[-1]):
                new_list.append(i)
        return new_list
    return []  # If the list has 0 elements.


# E. Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideally, the solution should work in "linear" time, making a single
# pass of both lists.
#
# NOTE - DO NOT use return sorted(sorted1 + sorted2) - that's too easy :-)
#
def linear_merge(sorted1, sorted2):
    """
    Given two lists sorted in increasing order, create and return a merged
    list of all the elements in sorted order. You may modify the passed in lists.
    Ideally, the solution should work in "linear" time, making a single
    pass of both lists.
    """
    new_lst = []
    ind1 = 0
    ind2 = 0
    for i in range(len(sorted1) + len(sorted2)):
        if(ind1 == len(sorted1)):
            new_lst.append(sorted2[ind2])
            ind2 += 1
        elif(ind2 == len(sorted2)):
            new_lst.append(sorted1[ind1])
            ind1 += 1
        elif(sorted1[ind1] < sorted2[ind2]):
            new_lst.append(sorted1[ind1])
            ind1 += 1
        else:
            new_lst.append(sorted2[ind2])
            ind2 += 1
    return new_lst


def test(got, expected):
    """ simple test() function used in main() to print
        what each function returns vs. what it's supposed to return. """

    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


def main():
    """ main() calls the above functions with interesting inputs,
        using test() to check if each result is correct or not. """

    print('\nmatch_ends')
    test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
    test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

    print('\nfront_x')
    test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']), ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']), ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
    test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']), ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])

    print('\nsort_last')
    test(sort_last([(1, 3), (3, 2), (2, 1)]), [(2, 1), (3, 2), (1, 3)])
    test(sort_last([(2, 3), (1, 2), (3, 1)]), [(3, 1), (1, 2), (2, 3)])
    test(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]), [(2, 2), (1, 3), (3, 4, 5), (1, 7)])

    print('\nremove_adjacent')
    test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
    test(remove_adjacent([1, 3, 3, 2, 2, 3]), [1, 3, 2, 3])
    test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
    test(remove_adjacent([]), [])

    print('\nlinear_merge')
    test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']), ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']), ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']), ['aa', 'aa', 'aa', 'bb', 'bb'])


if __name__ == '__main__':
    main()
