# Exercise 22: http://www.ling.gu.se/~lager/python_exercises.html
def correct(sentence):
    '''A function that takes a string and sees to it that 1) two or more 
       occurrences of the space character is compressed into one, 
       and 2) inserts an extra space after a period if the period is directly
       followed by a letter.'''
    
    new_sentence = ''
    
    for i in range(len(sentence)):
        # If it's the last character, we simply add it
        if i == len(sentence)-1: 
            new_sentence += (sentence[i])
        # If two spaces are found next to each other
        elif sentence[i] == ' ' and sentence[i+1] == ' ':
            pass
        # If a dot is not followed by a space
        elif sentence[i] == '.' and sentence[i+1] != ' ':
            new_sentence += (". ")
        else:
            new_sentence += (sentence[i])
            
    # EXTRA: We check there is not trailing space        
    if new_sentence[-1] == ' ':
        new_sentence = new_sentence[:-1]
            
    return new_sentence