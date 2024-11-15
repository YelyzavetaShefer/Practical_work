def decimal_to_binary(decimal_number):
    return bin(decimal_number)
def decimal_to_hexadecimal(decimal_number):
    return hex(decimal_number)
def binary_to_decimal(binary_number):
    return int(binary_number, 2)
def binary_to_hexadecimal(binary_number):
    decimal_number = int(binary_number, 2)
    return hex(decimal_number)
def hexadecimal_to_decimal(hexadecimal_number):
    return int(hexadecimal_number, 16)
def hexadecimal_to_binary(hexadecimal_number):
    decimal_number = int(hexadecimal_number, 16)
    return bin(decimal_number)
def convert_number():
    repeat = "yes"
    while repeat == "yes":
        number = input("Enter a number in decimal, binary (prefix 0b), or hexadecimal (prefix 0x) form: ")
        number_system = int(input("In which number system do you want to convert the number? Please write '2', '10' or '16': "))
        if number.startswith("0b"):
            if number_system == 2:
                print("Your number is already in binary.")
            elif number_system == 10:
                decimal_number = binary_to_decimal(number)
                print(f"Your number {number} in the decimal system is equal to {decimal_number}.")
            elif number_system == 16:
                hexadecimal_number = binary_to_hexadecimal(number)
                print(f"Your number {number} in the hexadecimal system is equal to {hexadecimal_number}.")
        if number.startswith("0x"):
            if number_system == 2:
                binary_number = hexadecimal_to_binary(number)
                print(f"Your number {number} in the binary system is equal to {binary_number}.")
            elif number_system == 10:
                decimal_number = hexadecimal_to_decimal(number)
                print(f"Your number {number} in the decimal system is equal to {decimal_number}.")
            elif number_system == 16:
                print("Your number is already in hexadecimal.")
        else:
            number = int(number)
            if number_system == 2:
                binary_number = decimal_to_binary(number)
                print(f"Your number {number} in the binary number system is equal {binary_number}.")
            elif number_system == 10:
                print("Your number is already in the decimal number system.")
            elif number_system == 16:
                hexadecimal_number = decimal_to_hexadecimal(number)
                print(f"Your number {number} in the hexadecimal number system is equal {hexadecimal_number}.")
        repeat = input("Do you want to convert another number? Please, enter yes or no: ").strip().lower()
    print("Thank you, goodbye!")
convert_number()