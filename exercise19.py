# Exercise 19: http://www.ling.gu.se/~lager/python_exercises.html
def bottles_of_beer(n = 99):
    '''A function that sings a popular American song.'''
    for _ in range(n):
        if n == 1:
            print str(n)+' bottle of beer on the wall, '+str(n)+' bottle of beer.'
        else:
            print str(n)+' bottles of beer on the wall, '+str(n)+' bottles of beer.'
        
        if n-1 == 1:
            print 'Take one down, pass it around, '+str(n-1)+' bottle of beer on the wall.\n'
        else:
            print 'Take one down, pass it around, '+str(n-1)+' bottles of beer on the wall.\n'
        
        n = n - 1