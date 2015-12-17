# Exercise 28: http://www.ling.gu.se/~lager/python_exercises.html

def find_longest_word(words):
    # Find the lenght of each word
    len_words = map(len, words)
    
    # Only takes the longest one
    return reduce(lambda a,b : a if a >= b else b, len_words)
    