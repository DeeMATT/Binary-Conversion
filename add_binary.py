"""
A function that adds two numbers together and returns their sum in binary
"""


def add_binary(a, b):
    numb = a + b
    return str(bin(numb))
    
    

"""
A different way to convert decimal to binary
without using the built-in 'bin' function in python

"""


def add_binary(a, b):   # A function to add integers and convert to its equivalent binary number
    decimal = a + b        # the integers are saved as 'a' and 'b' then added together
    if decimal > 0:
        # An empty string called binary to hold the remainders
        # from the division in converting the decimal to binary
        binary = ''

        while decimal > 0:     # A nested while loop to iterate the division of the decimal
            quotient = (decimal // 2)      # The decimal number is divided using floor division to save the whole number
            remainder = (decimal % 2)      # The modulo operator is used to divide the number so as to get the remainder
            binary += str(remainder)      # The remainder is converted to string and added to the empty string declared above

            # The whole number from the previous floor division
            # which is saved as 'quotient' is reassigned to 'decimal
            decimal = quotient

            # The while loop continues its iteration as long as the decimal is above 'int 0'

    return binary[::-1]     # This is to return the remainders in reverse order which then makes up the binary
