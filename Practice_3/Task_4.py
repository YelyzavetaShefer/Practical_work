data = (input("Please, write your information: "))
letters = 0
digits = 0
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
for i in data:
    if i in alphabet:
        letters += 1
    if i in numbers:
            digits += 1
print(f"Letters {letters}, Digits {digits}")
