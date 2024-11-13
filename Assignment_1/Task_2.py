import statistics

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit -32) * 5/9
celsius_temperatures = []
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
for day in days:
    fahrenheit = int(input(f"Temperature in Fahrenheit on {day}: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    celsius_temperatures.append(celsius)
    if celsius < 10:
        print("Cold: below 10°C")
    elif 10 <= celsius <= 28:
        print("Warm: 10°C to 28°C")
    elif 28 < celsius <= 36:
        print("Hot:above 28°C")
    elif celsius > 36:
        print("Very hot: above 36°C")
average_temperature = statistics.mean(celsius_temperatures)
min_temperature = min(celsius_temperatures)
max_temperature = max(celsius_temperatures)
print(f"Average temperature: {average_temperature}°C")
print(f"Minimum temperature: {min_temperature}°C")
print(f"Maximum temperature: {max_temperature}°C")
