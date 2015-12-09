# Exercise 21: http://www.ling.gu.se/~lager/python_exercises.html
def char_freq(sentence):
    '''A function takes a string and builds a frequency 
       listing of the characters contained in it.'''
    letters = {}
    for c in sentence:
        if c not in letters:
            letters[c] = 1
        else:
            letters[c] += 1
    return letters