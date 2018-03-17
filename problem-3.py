"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""
import sys

# Hacking the recursion limit
sys.setrecursionlimit(10000)

i = 1
given_number = 600851475143
largest_prime_factor = i

def factorial(prime_factor, given):
    answer = given

    if is_factorable(prime_factor, given):
        answer = given / prime_factor
        # print("Current answer: " + str(int(answer)))
        print("The answer for (" + str(given) + " / " + str(prime_factor) + ") is " + str(int(answer)))

    if answer == 1:
        return prime_factor
        
    return factorial(prime_factor+1, answer)

def is_factorable(number, given):
    return given % number == 0


largest_prime_factor = factorial(2, given_number)
print("The largest prime factor is: " + str(largest_prime_factor))