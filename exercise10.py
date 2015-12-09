# Exercise 10: http://www.ling.gu.se/~lager/python_exercises.html

def overlapping(list1, list2):
    '''A function that takes two lists and returns True if they
       have at least one member in common, False otherwise.'''
    boo = False
    for j in list1:
        for z in list2:
            if j == z:
                boo = True
                break
        if boo: # No reason to loop if boo is True
            break
    return boo