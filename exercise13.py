# Exercise 13: http://www.ling.gu.se/~lager/python_exercises.html

def max_in_list(array):
    '''A function that takes a list of numbers and returns the largest one.'''
    max_value = -float("inf") # -Infinite is by definition the lowest value
    for n in array:
        if n >= max_value:
            max_value = n
    return max_value