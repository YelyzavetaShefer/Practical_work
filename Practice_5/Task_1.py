def find_max (a, b):
   return max(a, b)
print(find_max(6, 4))

def find_max_of_three(x, y, z):
    if x > y and x > z:
        return x
    elif y > x and y > z:
        return y
    else:
        return z
print(find_max_of_three(10, 3, 11))

