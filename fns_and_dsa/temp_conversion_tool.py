# temp_conversion_tool.py

# --- Global Conversion Factors ---
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5


# --- Conversion Functions ---
def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius using global conversion factor.
    Formula: (F - 32) * (5/9)
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit using global conversion factor.
    Formula: (C * (9/5)) + 32
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


# --- Main Program ---
def main():
    print("--- Temperature Conversion Tool ---")

    try:
        temp = float(input("Enter the temperature value: "))  # Validate numeric input
        unit = input("Is this in Celsius (C) or Fahrenheit (F)? ").strip().upper()

        if unit == "F":
            result = convert_to_celsius(temp)
            print(f"{temp}°F is equal to {result:.2f}°C")

        elif unit == "C":
            result = convert_to_fahrenheit(temp)
            print(f"{temp}°C is equal to {result:.2f}°F")

        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")


if __name__ == "__main__":
    main()