"""
Challenge #2:
​
Write a function that takes an integer `minutes` and converts it to seconds.
​
Examples:
- convert(5) ➞ 300
- convert(3) ➞ 180
- convert(2) ➞ 120
- convert(-10) -> -600 
"""
def convert(minutes):
    """
    Input: int 
    Output: int 
​
    What we received a negative integer?
    1. Do the same thing  
    2. Check if the input int >= 0, and only multiply by 60 if it is 
​
    We know that there are 60 seconds in a minute 
    Given n minutes, we can convert that into seconds with the formula
    n * 60 
    """
​
    # return minutes * 60 
​
    answer = minutes * 60 
    return answer
