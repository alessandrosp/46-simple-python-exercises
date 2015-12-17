# Exercise 30: http://www.ling.gu.se/~lager/python_exercises.html

def translate(words):
    '''A function that takes a list of English words and
       returns a list of Swedish words.'''
    dictionary = {"merry":"god", "christmas":"jul",
                  "and":"och", "happy":"gott", "new":"nytt", "year":"år"}
    
    # new_words = [dictionary[w] for w in words]
    new_words = map(lambda w: dictionary[w], words)
    return new_words