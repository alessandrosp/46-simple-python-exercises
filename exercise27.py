# Exercise 27: http://www.ling.gu.se/~lager/python_exercises.html

def map_words1(words): # 1) Using a for-loop
    len_words = []
    
    for w in words:
        len_words.append(len(w))
    
    return len_words

def map_words2(words): # 2) Using the higher order function map()
    return map(len, words)

def map_words3(words): # 3) Using list comprehensions
    return [len(w) for w in words]