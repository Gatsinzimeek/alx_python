def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius
    fahrenheit_temperature = float(input("Enter the temperature in Fahrenheit: "))
    celsius_temperature = convert_to_celsius(fahrenheit_temperature)
print("Temperature in Celsius:", celsius_temperature)
