"""
Challenge #9:
​
Write a function that creates a dictionary with each (key, value) pair being
the (lower case, upper case) versions of a letter, respectively.
​
Examples:
- mapping(["p", "s"]) ➞ { "p": "P", "s": "S" }
- mapping(["a", "b", "c"]) ➞ { "a": "A", "b": "B", "c": "C" }
- mapping(["a", "v", "y", "z"]) ➞ { "a": "A", "v": "V", "y": "Y", "z": "Z" }
​
Notes:
- All of the letters in the input list will always be lowercase.
"""
def mapping(letters):
    # Your code here
​
    # we can write this tersely with a dictionary comprehension
    # return {letter: letter.upper() for letter in letters}
​
    # more explicitly
    d = {}
​
    for letter in letters:
        # set the key as the lowercase letter and the value
        # as the same letter uppercased 
        d[letter] = letter.upper()
​
    return d

    # def mapping(letters)

    # d = {}

    # for letter in letters:
    #     d[letter] = letter.upper()