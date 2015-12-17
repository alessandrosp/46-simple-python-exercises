# Exercise 31: http://www.ling.gu.se/~lager/python_exercises.html

def new_map(f, iterable):
    '''Implements map()'''
    
    mapped = []
    for i in iterable:
        mapped.append(f(i))
        
    return mapped

def new_filter(f, iterable):
    '''Implements filter()'''
    
    filtered = []
    for i in iterable:
        if f(i):
            filtered.append(i)
    
    return filtered

def new_reduce(f, iterable):
    '''Implements reduce()'''
    
    while len(iterable) > 1:
        # Prepend the value of f(a,b) and then it eliminates a and b from
        # the list; when the list has just 1 item, it returns that item
        iterable.insert(0, f(iterable[0],iterable[1]))
        iterable.pop(1)
        iterable.pop(1)
        
    return iterable