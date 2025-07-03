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
    modes = "Your modes are:" \
    "1. From binary to normal chararcters\n" \
    "2. From binary to ASCII\n" \
    "3. From ASCII to its ASCII number\n" \
    "4. From ASCII to binary\n" \
    "5. From normal characters to binary"
    print(modes)
    mode  = input("Enter your mode(1,2,3,4 or 5)")

    if mode == "1":
        binary_input = input("Enter 8-bit binary strings separated by spaces: ").split()
        result = return_normal_char(binary_input)
        print("Characters:", ''.join(result))
    
    elif mode == "2":
        ascii_binaries = return_ascii()
        print("ASCII binaries (0-255):")
        print(ascii_binaries)
    
    elif mode == "3":
        char_input = input("Enter a character: ")
        if len(char_input) != 1:
            print("INVALID")
        else:
            print("ASCII number:", ord(char_input))
        
    elif mode == "4":
        char_input = input("Enter a character: ")
        if len(char_input) != 1:
            print("INVALID")
        else:
            print("Binary:", calc_normal_num(ord(char_input)))
        
    elif mode == "5":
        text = input("Enter text: ")
        binaries = [calc_normal_num(ord(c)) for c in text]
        print("Binary representation:", ' '.join(binaries))
    
    else:
        print("INVALID MODE")
    print("Thank you for using BinaryConvert.")

main()