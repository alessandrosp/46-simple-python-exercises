# Exercise 18: http://www.ling.gu.se/~lager/python_exercises.html
import string

def is_pangram(sentence):
    '''A function that checks whether a string is a pangram.'''
    clean = sentence.replace(" ","").lower()
    if len(clean) < 26:
        return False
    
    counter = set()
    for c in clean:
        if c in string.ascii_lowercase:
            counter.add(c)
        if len(counter) == 26:
            return True
    
    return False
        