#Step 1: Define Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

#Step 2: Implement Conversion functions
def convert_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
def convert_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit"""
    return (celsius *CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

#Step 3: User Interaction and Input validation
def main():
    try:
        #Ask user for temperature
        temp = float(input("Enter the temperature to convert: "))

        #Ask user to specify the unit
        unit = input("Is the temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        #Perform Conversion based on the unit
        if unit == 'C':
            converted_temp = convert_to_fahrenheit(temp)
            print(f"{temp}\u00B0C is {converted_temp}\u00B0F")
        elif unit == 'F':
            converted_temp = convert_to_celsius(temp)
            print(f"{temp}\u00B0F is {converted_temp}\u00B0C")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()