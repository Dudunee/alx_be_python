task = input("Enter your task: ")
priority = input("high, medium, low?: ")
time_bound = input("is it time-bound? (yes or no): ")
match priority:
    case "high":
        if time_bound == "yes":
            reminder = f"{task}" " is a high priority task that requires immediate attention today!."
            print(f"{reminder}")
match priority:
    case "low":
        if time_bound == "no":
            reminder = f"{task}" " is a low priority task. Consider completing it when you have free time."
            print(f"{reminder}")
