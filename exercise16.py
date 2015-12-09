# Exercise 16: http://www.ling.gu.se/~lager/python_exercises.html

def filter_long_words(words, n):
    '''A function that takes a list of words and an integer n and
       returns the list of words that are longer than n.'''
    return [w for w in words if len(w) > n]