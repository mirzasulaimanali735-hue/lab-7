# Temperature Converter
# A small program for practising Git and GitHub.
# It converts a temperature from Celsius to Fahrenheit.
#
# How to run it:  python temperature_converter.py

# Ask the user for a temperature in Celsius
celsius = float(input("Temperature in Celsius: "))

# Convert to Fahrenheit
fahrenheit = celsius * 9 / 5 + 32

# Show the result
print("1 Fahrenheit:", fahrenheit)
# Convert to kelvin
kelvin = celsius + 273.15
#show the result
print("1 Kelvin:", kelvin)