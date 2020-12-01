"""
Challenge #5:
​
Create a function that returns a list of strings sorted by length in ascending
order. If two strings have the same length, sort those in alphabetical order. 
​
Examples:
- sort_by_length(["a", "ccc", "dddd", "bb"]) ➞ ["a", "bb", "ccc", "dddd"]
- sort_by_length(["a", "ccc", "d", "bbbb"]) -> ['a', 'd', 'ccc', 'bbbb'] 
- sort_by_length(["apple", "pie", "shortcake"]) ➞ ["pie", "apple", "shortcake"]
- sort_by_length(["may", "april", "september", "august"]) ➞ ["may", "april", "august", "september"]
- sort_by_length([]) ➞ []                                     
"""
def sort_by_length(lst):
    '''
    input: list of strings, where all strings might be of different length 
    output: list of strings, where the strings are sorted by length in ascending order
​
    if we're given an empty list, return an empty list 
​
    what does "sorted by length in ascending order" mean? 
    shorter words come first 
​
    if two strings have the same length, sort those in alphabetical order 
​
    can we use the builtin `sort` function for this? 
    '''
    # use the `sort` method on lists 
    # lst.sort(key=len)
    # lst.sort(key=lambda x: len(x)) # from our testing, the `sort` method sorts in alphabetical order 
    
    # to properly sort strings that have the same length, we need to specifiy two 
    # "priorities": what to do with two strings that have different lengths
    # what to do with two strings that have the same length 
    lst.sort(key=lambda x: (len(x), x))
​
    # how do tell the `sort` method to sort by length? 
    # pass in the `len` function as the `key` or, pass in an anonymous lambda
    # function that says to sort by the length of each list element 
​
    return lst
​
print(sort_by_length([]))
print(sort_by_length(["a", "ccc", "dddd", "bb"]))
print(sort_by_length(["apple", "pie", "shortcake"]))
print(sort_by_length(['z', 'bbbb', 'ccc', 'd', 'e', 'a']))

# or 

# def sort_by_length(1st):
#     return sorted(1st, key=len)