word = input("Please, write a word: ")
symbol_1 = input("Please, write a symbol that should go first: ")
symbol_2 = input("Please, write a symbol that should go after the first one: ")
if symbol_1 not in word or symbol_2 not in word:
    print(False)
if symbol_1 == symbol_2:
    print(False)
symbol_1 = word.find(symbol_1)
symbol_2 = word.find(symbol_2)
if symbol_1 < symbol_2 and symbol_1 + 1 == symbol_2:
    print(True)
else:
    print(False)