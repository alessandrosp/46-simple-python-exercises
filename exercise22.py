# Exercise 22: http://www.ling.gu.se/~lager/python_exercises.html
def ROT_13(sentence):
    '''A function that implements a simple ROT-14 cipher.'''
    key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 
           'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c', 
           'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k',
           'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S', 
           'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A', 
           'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I', 
           'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}
    new_sentence = ''
    for c in sentence:
        if c not in key:
            new_sentence += c
        else:
            new_sentence += key[c]
    
    return new_sentence