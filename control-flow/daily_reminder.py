# daily_reminder.py

# Prompt user for inputs
task = input("Enter your task: ")
priority = input("Enter the task's priority (high/medium/low): ").lower()
time_bound = input("Is the task time-bound? (yes/no): ").lower()

# Loop once to simulate a reminder system (could be extended for multiple reminders)
while True:
    match priority:
        case "high":
            message = f"Reminder: '{task}' is a HIGH priority task."
        case "medium":
            message = f"Reminder: '{task}' is a medium priority task."
        case "low":
            message = f"Reminder: '{task}' is a low priority task."
        case _:
            message = f"Reminder: '{task}' has an unspecified priority."

    # Include a note that is time-sensitive
    if time_bound == "yes":
        message += " It requires immediate attention today!"

    # Print the reminder
    print(message)

    # Conclude the loop after displaying the reminder a single time
    break
