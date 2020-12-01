"""
Challenge #10:
​
Create a function that applies a discount d to every number in the list.
​
Examples:
- get_discounts([2, 4, 6, 11], "50%") ➞ [1, 2, 3, 5.5]
- get_discounts([10, 20, 40, 80], "75%") ➞ [7.5, 15, 30, 60]
- get_discounts([100], "45%") ➞ [45]
​
Notes:
- The discount is the percentage of the original price (i.e the discount of
"75%" to 12 would be 9 as opposed to taking off 75% (making 3)).
- There won't be any awkward decimal numbers, only 0.5 to deal with.
"""
def get_discounts(nums, percentage):
    '''
    Input:
    nums: List of ints 
    percentage: string representing the discount percentage to be applied
​
    Output: List of floats 
​
    For each number in the `nums` list, we need to multiply it by the 
    discount percentage 
​
    One issue though is that the discount percentage is a string, i.e.,
    we won't get the desired result if we just multiple each number 
    by the percentage string 
​
    So we need to convert the percentage string into a decimal value that 
    we can actually multiply by a number 
​
    "45%" needs to be converted to 0.45
    "75%" needs to be converted to 0.75
    "100%" would be converted to 1.0 
​
    Once we've done the conversion, we can multiply each num in the nums 
    list by the decimal and return the result 
    '''
    # Your code here
    # get the numbers in the `percentage` string
    # don't get the last element in the string, which is the "%" sign
    # divide the number by 100 to get the corresponding decimal
    discount = int(percentage[:-1]) / 100
​
    # using a list comprehension
    # return [n * discount for n in nums]
​
    discounted = []
​
    for n in nums:
        discounted.append(n * discount)
​
    return discounted
​
​
print(get_discounts([2, 4, 6, 11], "50%"))
print(get_discounts([10, 20, 40, 80], "75%"))