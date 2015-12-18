# Exercise 34: http://www.ling.gu.se/~lager/python_exercises.html
import string

def generate_n_chars(n, c):
    '''A function that takes an integer n and a character c and
       returns a string, n characters long, consisting only of c.'''
    new_string = ''
    for _ in range(n):
        new_string = new_string + c
    return new_string

def char_freq_table(filename, mode = 'print'):
    '''A procedure that builds a frequency listing of the characters contained
       in the file. The parameter 'mode' accepts three possible
       arguments: print (default), graphical or silent. You can test it
       with char_freq_table("exercise34-text.txt")'''
    
    # Note: we could have used collections.Counter but
    # that would have been no fun at all. :)
    counter = {} # The actual counting
    letters = set() # Unique characters that have been counted
    
    # We start the counting
    f = open(filename, 'r')
    for line in f:
        for char in line.lower().replace('\n','').replace(' ',''):
            if char in letters:
                counter[char] += 1
            else:
                letters.add(char)
                counter[char] = 1
    
    # Printing according to "mode"
    if mode == 'print':
        print "\nHello, sir.\nThe file contained the following characters:\n"
        for letter in string.ascii_lowercase+string.punctuation:
            if letter in letters:
                print letter+" : "+str(counter[letter])
    elif mode == 'graphical':
        print "\nHello, sir.\nThe file contained the following characters:\n"
        for letter in string.ascii_lowercase+string.punctuation:
            if letter in letters:
                print letter+" : "+str(generate_n_chars(counter[letter], '+'))
    elif mode == 'silent':
        return counter