# Exercise 29: http://www.ling.gu.se/~lager/python_exercises.html

def is_longer(word, n):
    '''Given a word and a number n returns True if
       len(word) > n, False otherwise.'''
    return len(word) > n

def filter_long_words(words, n):
    '''Given a list of words and a number n it returns a list 
    with only the words whose lenght is > then n. '''
    # List comprehension would have been a better 
    # choice here, but the exercise requested the use of filter()
    return filter(lambda w: is_longer(w, n), words)