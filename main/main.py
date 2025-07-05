# /main/main.py
"""
This is the main file. It has many functions:
1. binary_equ: Find the equivalent of a binary number
2. 
"""
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
                # Calc number
                result = 0
                if strnum[0] == 0:
                    continue
                elif strnum[0] == 1:
                    result + 1
                    continue
                if strnum[1] == 0:
                    continue
                elif strnum[1] == 1:
                    result + 2
                    continue
                if strnum[2] == 0:
                    continue
                elif strnum[2] == 1:
                    result + 4
                    continue
                if strnum[3] == 0:
                    continue
                elif strnum[3] == 1:
                    result + 8
                    continue
                if strnum[4] == 0:
                    continue
                elif strnum[4] == 1:
                    result + 16
                    continue
                if strnum[5] == 0:
                    continue
                elif strnum[5] == 1:
                    result + 32
                    continue
                if strnum[6] == 0:
                    continue
                elif strnum[6] == 1:
                    result + 64
                    continue
                if strnum[7] == 0:
                    continue
                elif strnum[7] == 1:
                    result + 128
                    continue
                return result

    else: #type:ignore
        raise ValueError("Input must be an 8-bit binary number") # strnum is not 8 chars long
        