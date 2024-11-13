temperatures_in_Celsius = [0, 20, 37, 100]
temperature_in_Fahrenheit = [9/5 * temperature + 32 for temperature in temperatures_in_Celsius]
print(f"The temperature in Fahrenheit is equal to {temperature_in_Fahrenheit}.")