# Exercise 6: http://www.ling.gu.se/~lager/python_exercises.html

def sum(nums):
    '''A function that sums all the values in a list.'''
    a = 0
    for i in nums:
        a += i
    return a

def multiply(nums):
    '''A function that multiplies all the values in a list.'''
    m = 1
    for i in nums:
        m = m * i
    return m