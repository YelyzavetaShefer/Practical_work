def decimal_to_binary(decimal_number):
    return bin(decimal_number)
def binary_to_decimal(binary_number):
    return int(binary_number, 2)
def convert_number():
    repeat = "yes"
    while repeat == "yes":
        number = input("Enter a number in decimal form or binary form with the prefix 0b: ")
        if number.startswith("0b"):
                decimal_number = binary_to_decimal(number)
                print(f"Your number {number} in the decimal system is equal to {decimal_number}.")
        else:
            binary_number = int(number)
            binary_number = bin(binary_number)
            print(f"Your number {number} in the binary number system is equal {binary_number}.")
        repeat = input("Do you want to convert another number? Please, enter yes or no: ").strip().lower()
    print("Thank you, goodbye!")
convert_number()










