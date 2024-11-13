data = input("Please enter any word or sentence: ")
count_of_vowels = 0
vowels = "aeiouyAEIOUY"
for i in data:
    if i in vowels:
        count_of_vowels += 1
print(count_of_vowels)