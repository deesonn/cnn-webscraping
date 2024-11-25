'''
Name: Daniel Nguyen
'''

# Function convert celsius to fahrenheit
def celsiusToFahrenheit(c):
    # To fahrenheit formula
    celcius = round(c * (9 / 5) + 32, 2)
    return celcius

def fahrenheitToCelsius(f):
    # To celsius formula
    fahrenheit = round((f - 32) * (5/9), 2)
    return fahrenheit

def main():
    # Prompt user for a temperature and their desired conversion type
    try:
        user_choice = float(input("What would you like to do? \n" +
                                "1. Convert Celsius to Fahrenheit \n" +
                                "2. Convert Fahrenheit to Celsius \n"))
        if user_choice == 1:
            celsius = float(input("Enter a degree in Celsius: "))
            # Call formula function 
            print(f"{celsius} degree Celsius to Fahrenheit is: {celsiusToFahrenheit(celsius)}") # Make sure you pass in celsius user input into function
        elif user_choice == 2:
            fahrenheit = float(input("Enter a degree in Fahrenheit: "))
            # Call formula function 
            print(f"{fahrenheit} to Fahrenheit is: {fahrenheitToCelsius(fahrenheit)}") # Make sure you pass in celsius user input into function
        else:
            print("Invalid input. Must choose between 1 or 2. Please try again. ")

    except ValueError:
        print("Invalid input. Please try again. ")

main()