# Exercise 15: http://www.ling.gu.se/~lager/python_exercises.html

def map_length(words):
    '''A function that that maps a list of words into a list of 
       integers representing the lengths of the correponding words.'''
    list_length = []
    for w in words:
        list_length.append(len(w))
    return list_length

def find_longest_word(words):
    '''A function that that takes a list of words
       and returns the length of the longest one.'''
    return max(map_length(words))