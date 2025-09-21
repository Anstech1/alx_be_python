# daily_reminder.py

# Prompt for a single task
task = input("Enter your task: ")
time_bound = input("Is it time-bound? (yes/no): ").lower()
priority = input("Enter priority (high/medium/low): ").lower()


# Simple loop (runs once for this demo — could be extended for repeated reminders)
while True:
    # Use match-case for priority handling
    match priority:
        case "high":
            message = f"Reminder: '{task}' is a high priority task"
        case "medium":
            message = f"Reminder: '{task}' is a medium priority task"
        case "low":
            message = f"Note: '{task}' is a low priority task"
        case _:
            message = f"Reminder: '{task}' has an unspecified priority"

    # Add time sensitivity handling
    if time_bound == "yes":
        message += " that requires immediate attention today!"
    else:
        if priority == "low":
            message += ". Consider completing it when you have free time."
        else:
            message += "."

    # Print the customized reminder
    print("\n" + message)

    # End loop after one reminder
    break   
