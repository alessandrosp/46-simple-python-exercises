# Exercise 20: http://www.ling.gu.se/~lager/python_exercises.html
def translate(words):
    '''A function that takes a list of English words and
       returns a list of Swedish words.'''
    new_words = []
    dictionary = {"merry":"god", "christmas":"jul",
                  "and":"och", "happy":"gott", "new":"nytt", "year":"år"}
    
    new_words = [dictionary[w] for w in words]
    
    return new_words