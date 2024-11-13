values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even = 0
odd = 0
for number in values:
    if number % 2 == 0:
        even += 1
    if number % 2 == 1:
        odd += 1


print(f"Number of even numbers: {even} \nNumber of odd numbers: {odd}")