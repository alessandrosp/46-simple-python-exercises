# Exercise 5: http://www.ling.gu.se/~lager/python_exercises.html

def is_vowel(char):
    '''A function that given a character returns True if it's a vowel.'''
    return char in ('a','e','i','o','u')

def translate(to_translate):
    '''Given a string, it doubles consonants and place an "o" in between.'''
    new_string = ''
    for c in to_translate:
        if is_vowel(c) or c == ' ':
            new_string = new_string + c
        else:
            new_string = new_string + c + 'o' + c
    return new_string