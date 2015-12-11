# Exercise 24: http://www.ling.gu.se/~lager/python_exercises.html
# For better performance (and easier code) use: endswith().
import re

def make_3sg_form(verb):
    '''A function which given a verb in infinitive form returns
       its third person singular form.'''
    
    new_form = ''
    
    # If the verb ends in y, remove it and add ies
    if re.match('[a-z]+y$',verb.lower()): 
        new_form = verb[:-1] + 'ies'
        
    # If the verb ends in o, s, x or z, add es
    elif re.match('[a-z]+[osxz]$',verb.lower()): 
        new_form = verb + 'es'
        
    # If the verb ends in ch, sh, add es
    elif re.match('[a-z]+(sh|ch)$',verb.lower()): 
        new_form = verb + 'es'
        
    # By default just add s
    else: 
        new_form = verb + 's'
        
    return new_form