# Exercise 33: http://www.ling.gu.se/~lager/python_exercises.html

def reverse(to_reverse):
    '''A function that reverses a string.'''
    new_string = ''
    for c in to_reverse:
        new_string = c + new_string
    return new_string

def check_semordnilap(words, index):
    '''Given a list of words and an index, it checks whether words contains a
       semordnilap for words[i] only checking words[i:]. If found, it returns
       the both the words as a tuple.'''
    to_check = words[index]
    to_return = []
    for w in words[index:]:
        if to_check == reverse(w):
            return (to_check,w)   

def print_semordnilap_from_file(filename):
    '''Given a text filename, it finds semordnilaps and print them. You 
       can test it using print_semordnilap_from_file("exercise33-text.txt").'''
    f = open(filename, 'r')
    words = [line.replace('\n','').lower() 
             for line in f]
    f.close()
    
    semordnilaps = [check_semordnilap(words,i) 
                    for i in range(len(words)) 
                    if check_semordnilap(words,i) is not None]
    
    print "\nHello, sir.\nI found the following semordnilaps:\n"
    for s in semordnilaps:
        print s[0]+" "+s[1]