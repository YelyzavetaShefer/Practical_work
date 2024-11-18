


def decimal_to_binary(decimal_number):
    return bin(decimal_number)


def binary_to_decimal(binary_number):
    return int(binary_number, 2)


def convert_number():
    repeat = "yes"
    while repeat == "yes":
        number = input("Enter a number in decimal form or binary form with the prefix 0b: ")
        if number.startswith("0b"):
            binary_number = number[2:]
            if not binary_number or not all(symbol in "01" for symbol in binary_number):
                print("Invalid binary format. Please, enter a binary number with only 0s and 1s after '0b'.")
                continue
            decimal_number = binary_to_decimal(number)
            print(f"Your number {number} in the decimal system is equal to {decimal_number}.")
        elif number.isdigit():
            binary_number = int(number)
            binary_number = bin(binary_number)
            print(f"Your number {number} in the binary number system is equal {binary_number}.")
        else:
            print("Invalid decimal format. Please enter a valid decimal number without letters or special symbols.")
            continue
        repeat = input("Do you want to convert another number? Please, enter yes or no: ").strip().lower()
    print("Thank you, goodbye!")
convert_number()










