#!/usr/bin/python3
'''
Complete each function below so that the test cases pass.
Your solutions should use the map and filter functions,
and not for loops or list comprehensions.
'''


def evens(n):
    '''
    Returns a list of even numbers from 0 to n inclusive.
    >>> evens(10)
    [0, 2, 4, 6, 8, 10]
    >>> evens(11)
    [0, 2, 4, 6, 8, 10]
    >>> evens(0)
    [0]
    >>> evens(1)
    [0]
    >>> evens(-1)
    []
    '''
    all_numbers = list(range(n+1))
    even = filter(lambda i: (i % 2 == 0), all_numbers)
    return list(even)


def threes(n):
    '''
    Returns list of all numbers from 0 to n inclusive that contain the digit 3

    >>> threes(2)
    []
    >>> threes(3)
    [3]
    >>> threes(10)
    [3]
    >>> threes(20)
    [3, 13]
    >>> threes(50)
    [3, 13, 23, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 43]
    '''
    all_numbers = list(range(n+1))

    def contain3(n):
        if '3' in str(n):
            return True
        else:
            return False

    three = filter(contain3, all_numbers)
    return list(three)


def small_words(text):
    '''
    Returns list of all words in input text less than 5 characters long.

    HINT:
    Recall that text.split() converts the text variable into a list of words.

    >>> small_words('this is a simple test case')
    ['this', 'is', 'a', 'test', 'case']
    >>> small_words('really enormous words')
    []
    >>> small_words('')
    []
    >>> small_words('a big word is bad')
    ['a', 'big', 'word', 'is', 'bad']
    '''
    list_words = list(text.split())
    less_than_5 = filter(lambda i: len(i) < 5, list_words)
    return list(less_than_5)


def squares(n):
    '''
    Returns a list of all square number between 1 and n inclusive.
    Recall that the nth square number is defined to be n*n.

    >>> squares(1)
    [1]
    >>> squares(2)
    [1, 4]
    >>> squares(3)
    [1, 4, 9]
    >>> squares(10)
    [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    '''
    numbers = list(range(1, n+1))
    squared_numbers = list(map(lambda n: n * n, numbers))
    return squared_numbers


def lengths(strings):
    '''
    Given list of strings, returns list of the lengths of the strings.

    >>> lengths([])
    []
    >>> lengths(['test'])
    [4]
    >>> lengths(['this','is','a','test'])
    [4, 2, 1, 4]
    '''
    string_length = list(map(lambda s: len(s), strings))
    return string_length
