# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    """
    Displays the current date and time in YYYY-MM-DD HH:MM:SS format
    """
    current_date = datetime.now()  # Get current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current Date and Time: {formatted_date}")
    return current_date  # Return for reuse


def calculate_future_date(days):
    """
    Calculates and displays the future date after adding given number of days.
    """
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    formatted_future = future_date.strftime("%Y-%m-%d")
    print(f"Future Date after {days} days: {formatted_future}")
    return future_date


def main():
    print("--- Date and Time Explorer ---")
    
    # Part 1: Show current datetime
    display_current_datetime()
    
    # Part 2: Calculate future date
    try:
        days = int(input("Enter number of days to add: "))
        calculate_future_date(days)
    except ValueError:
        print("Please enter a valid integer for days.")


if __name__ == "__main__":
    main()
