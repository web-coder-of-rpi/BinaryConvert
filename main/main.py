# /main/main.py
'''
This is the main file. It has many functions:
1. binary_equ: Find the equivalent of a binary number
2. 
'''
# Find the equivalent normal number of a 8-bit binary number
def binary_equ(binary_number):
    strnum = str(binary_number)  # Convert int to str
    print("Checking number...")
    if len(strnum) == 8: # strnum is 8 characters long?
        # Check each place in strnum
        for i in range(8):
            if strnum[i] != '0' and strnum[i] != '1': # If the character is not 0 or 1:
                raise ValueError("Input must be an 8-bit binary number") # Raise a ValueError
            else:

    else: #type:ignore
        raise ValueError("Input must be an 8-bit binary number") # strnum is not 8 chars long
        