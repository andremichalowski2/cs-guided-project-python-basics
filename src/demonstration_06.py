"""
Challenge #6:
​
Create a function that takes a string, checks if it has the same number of "x"s
and "o"s and returns either True or False.
​
- Return a boolean value (True or False).
- The string can contain any character.
- When no x and no o are in the string, return True.
​
Examples:
- XO("ooxx") ➞ True
- XO("xooxx") ➞ False    3 x's, 2 o's 
- XO("ooxXm") ➞ True (Case insensitive)  2 o's 2 x's 
- XO("zpzpzpp") ➞ True (Returns True if no x and o)  0 x's 0 o's 
- XO("zzoo") ➞ False  0 x's 2 o's 
"""
def XO(txt):
    '''
    input: string that may or may not contain x's and o's 
    output: boolean indicating whether the string has the same number of x's and o's 
​
    Casing doesn't matter, treat capital and lowercase x's and o's as the same 
​
    When we walked through the examples ourselves, we essentially counted the number
    of x's and the number of o's
​
    If the number of x's and o's matched, return True, otherwise if they differ, 
    we return False 
    ''' 
    num_xs = 0
    num_os = 0
​
    # we need to make this logic case-insensitive 
    # we can do this by lowercasing every incoming letter 
​
    # this is how we loop through a string to get each letter 
    for letter in txt.lower():
        if letter == 'x':
            num_xs += 1
​
        # this does not need to be an `elif` because
        # we'll never get a letter that is both an 'x' and an 'o'  
        if letter == 'o':
            num_os += 1
​
    return num_xs == num_os
​
print(XO("ooxx"))
print(XO("xooxx"))
print(XO("ooxXm"))
print(XO("zpzpzpp"))
print(XO("zzoo"))