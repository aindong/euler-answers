"""
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""

largest_palindrome = 0

def reverse_string(number):
    number = str(number)
    result = ""
    for i in number:
        result = i + result
        
    return result

for i in range(999):
    for j in range(999):        
        # find the product of i and j
        product = i * j
        reverse = reverse_string(product)
        
        if str(product) == reverse:
            print("Reverse of(" + str(i) + "*" + str(j) + ") " + str(product) + " is " + reverse)
            print("Palindrome found: " + str(product))

            if product > largest_palindrome:
                largest_palindrome = product

print("Largest palindrome found is: " + str(largest_palindrome))