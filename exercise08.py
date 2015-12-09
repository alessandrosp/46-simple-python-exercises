# Exercise 8: http://www.ling.gu.se/~lager/python_exercises.html

def reverse(to_reverse):
    '''A function that reverses a string.'''
    new_string = ''
    for c in to_reverse:
        new_string = c + new_string
    return new_string

def is_palindrome(to_check):
    '''A function that recognizes palindromes.'''
    return to_check == reverse(to_check)