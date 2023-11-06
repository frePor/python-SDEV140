# This program converts temperatures in celcius to fahrenheit

while True:

    # Takes input from the user
    celsius = float(input("Enter temperature in Celsius: "))


    # Converts Celsius to Fahrenheit using the provided formula
    fahrenheit = (9/5) * celsius + 32

    # Displays the temperature in Fahrenheit
    print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit")
