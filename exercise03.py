# Exercise 3: http://www.ling.gu.se/~lager/python_exercises.html
def length(iterable):
    '''A function that given an iterable returns its length.'''
    length = 0
    for _ in iterable:
        length += 1
    return length