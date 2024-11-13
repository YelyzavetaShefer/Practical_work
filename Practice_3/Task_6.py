password = (input("Please, enter your passwort: "))
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
capital_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
character = "$#@]"
# довжина паролю
if len(password) < 6:
    print("Sorry, your password is too short. The password must contain at least 6 characters!")
elif len(password) > 16:
    print("Your password is too long. The password must contain no more than 16 characters!")
# мінімум одна маленька літера
has_lowercase_letter = any(symbol in lowercase_letters for symbol in password)
if has_lowercase_letter == False:
    print("Your password must contain at least one lowercase letter!")
 # мінімум одна велика літера
has_capital_letter = any(symbol in capital_letters for symbol in password)
if has_capital_letter == False:
  print("Your password must contain at least one capital letter!")
# мінімум одне число
has_number = any(symbol in numbers for symbol in password)
if has_number == False:
    print("Your password must contain at least one digit!")
# мінімум один символ
has_character = any(symbol in character for symbol in password)
if has_character == False:
    print("Your password must contain at least one special character such '$', '#' or '@'!")
else:
    print("Your password is correct:)")



