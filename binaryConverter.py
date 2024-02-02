import random

# Write a program that generates random 4 digit numbers of 0s and 1s and converts the generated number to base 10.
def BinaryConverter():
    # Generate a random 4-digit binary number
    binary_number = ''.join(random.choice('01') for _ in range(4))
    
    # Convert the binary number to base 10
    decimal_number = int(binary_number, 2)
    
    return binary_number, decimal_number
