# Prompt the user for input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Generate and print reminder based on priority and time-bound status
match priority:
    case "high":
        if time_bound == "yes":
            reminder = f"{task} is a high priority task that requires immediate attention today!"
            print(f"Reminder: {reminder}")
        else:
            reminder = f"{task} is a high priority task."
            print(f"Reminder: {reminder}")

    case "medium":
        if time_bound == "yes":
            reminder = f"{task} is a medium priority task that should be completed soon."
            print(f"Reminder: {reminder}")
        else:
            reminder = f"{task} is a medium priority task."
            print(f"Reminder: {reminder}")

    case "low":
        if time_bound == "no":
            reminder = f"{task} is a low priority task. Consider completing it when you have free time."
            print(f"Reminder: {reminder}")
        else:
            reminder = f"{task} is a low priority task."
            print(f"Reminder: {reminder}")

    case _:
        print("Invalid priority entered. Please enter 'high', 'medium', or 'low'.")


