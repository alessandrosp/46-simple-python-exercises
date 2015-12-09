# Exercise 17: http://www.ling.gu.se/~lager/python_exercises.html
import string

def reverse(to_reverse):
    '''A function that reverses a string.'''
    new_string = ''
    for c in to_reverse:
        new_string = c + new_string
    return new_string

def is_palindrome(to_check):
    '''A better function that recognizes palindromes ignoring punctuation,
       capitalization, and spacing. See exercise 08.'''
    exclude = set(string.punctuation) # Set of all punctuation marks
    exclude.add(' ') # Add the space
    # We clean for lowercase and punctuation
    to_check_clean = ''.join(c for c in to_check.lower() if c not in exclude)
    return to_check_clean == reverse(to_check_clean)