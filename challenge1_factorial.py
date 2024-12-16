
def factorial(num):
    if type(num) is int and num >= 0:    # checking weather num is an integer and its positive
        product = 1      # initialising the product variable and n, which is the increment counter 
        n = 1

        while n <= num:         # while condition to loop until n is less than or equal to num
            product = product * n       # storing the product of product and n variables
            n = n + 1   # increasing the counter by 1

        return product
    
    else:
        return None            # return None if the input does not satisfy the if condition
        


# This is an example of how your code will be called.
# Your function should return the factorial of the number.
# You can edit this code to try different testing cases, which
# will run before the challenge test cases.
number = 'spam spam spam spam' 
result = factorial(number)
print(result)