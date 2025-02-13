def binary_to_graycode(binary:str):
    if not all(bit in '01' for bit in binary):
        return "Invalid Binary Expression"

    gray:str = binary[0]

    #XOR operation
    for i in range(1,len(binary)):
        gray_bit = "1" if binary[i] != binary[i-1] else "0"
        gray += gray_bit

    return gray

   


def graycode_to_binary(graycode:str):
    if not all(bit in '01' for bit in graycode):
        return "Invalid Binary Expression"

    binary:str = graycode[0]

    #XOR operation
    for i in range(1,len(graycode)):
        binary_bit = "0" if graycode[i] == graycode[i-1] else "1"
        binary += binary_bit

    return binary

# print(binary_to_graycode("1101")) 
# print(graycode_to_binary("1001"))   

def main():
    while True:
        print('Code Converter Menu')
        print('1. Convert from binary to graycode')
        print('2. Convert from graycode to binary')
        print("3. exit")

        choice = input('Enter your choice (1-3)\n')
        if(choice == '1'):
            binary = input("Enter your binary number\n\n")
            print(f'Answer = {binary_to_graycode(binary)}')
        elif (choice == '2'):
            graycode = input('Enter your graycode\n')
            print(f'Answer = {graycode_to_binary(graycode)} \n\n')
        elif (choice == "3"):
            print('Thank you for using this converter\n')
            exit()
        else:
            print('Enter a valid choice')   



main()
