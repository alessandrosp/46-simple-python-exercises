# Exercise 9: http://www.ling.gu.se/~lager/python_exercises.html

def is_member(member, group):
    '''A function that takes a value x and a list of values a, and
       returns True if x is a member of a, False otherwise.'''
    boo = False
    for e in group:
        if e == member:
            boo = True
            break
    return boo