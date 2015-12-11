# Exercise 25: http://www.ling.gu.se/~lager/python_exercises.html
# For better performance (and easier code) use: endswith().
import re

def make_ing_form(verb):
    '''which given a verb in infinitive form 
       returns its present participle form.'''
    
    new_form = ''
    
    # If the verb ends in ie, change ie to y and add ing
    if re.match('[a-z]+ie$',verb.lower()): 
        new_form = verb[:-2] + 'ying'
        
    # If the verb ends in e, drop the e and add
    # -ing (if not exception: be, see, flee, knee, etc.)
    elif re.match('[a-z\d]+e$',verb.lower()): 
        if verb in ['be','see','flee','knee']:
            new_form = verb + 'ing'
        else:
            new_form = verb[:-1] + 'ing'
    
    # For words consisting of consonant-vowel-consonant, double 
    # the final letter before adding ing        
    elif re.match('[^aeiou][aeiou][^aeiou]$', verb.lower()):
        new_form = verb + verb[-1] + 'ing'
    
    # By default add 'ing'
    else:
        new_form = verb + 'ing'
        
    return new_form