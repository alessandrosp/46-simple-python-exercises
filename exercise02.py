# Exercise 2: http://www.ling.gu.se/~lager/python_exercises.html
def max_of_three(first_n, second_n, third_n):
    '''A function that given three numbers returns the largest of them.'''
    if first_n >= second_n and first_n >= third_n:
        return first_n
    elif second_n >= third_n:
        return second_n
    else:
        return third_n