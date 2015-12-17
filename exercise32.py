# Exercise 32: http://www.ling.gu.se/~lager/python_exercises.html
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
    exclude.add("\n") # Add the new line
    # We clean for lowercase and punctuation
    to_check_clean = ''.join(c for c in to_check.lower() if c not in exclude)
    return to_check_clean == reverse(to_check_clean)

def palindrome_recogniser(filename):
    '''Given a text filename, it prints every line that is a palindrome. You 
       can test it using palindrome_recogniser("exercise32-text.txt").'''
    file_to_read = open(filename, 'r')
    
    # For each line we check whether it's palindrome
    for line in file_to_read:
        if is_palindrome(line):
            print line
            
    file_to_read.close()
