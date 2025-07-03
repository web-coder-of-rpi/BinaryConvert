# Function for calculating binary numbers
def calc_binary_num(num):
    num_str = str(num)
    if len(num_str) != 8 or not all(c in '01' for c in num_str):
        return "INVALID"
    result = int(num_str, 2)
    return result
# Function for makeing numbers binary
def calc_normal_num(bnum):
    if not isinstance(bnum, int) or bnum < 0 or bnum > 255:
        return "INVALID"
    return format(bnum, '08b')

# Function to return a list of ASCII
def return_ascii():
    ascii_list = [i for i in range(256)]
    return [format(i, '08b') for i in ascii_list]

def return_normal_char(array):
    # Converts a list of 8-bit binary strings to their ASCII characters
    return [chr(int(b, 2)) for b in array]

def main():
    print("Welcome to BinaryConvert!")