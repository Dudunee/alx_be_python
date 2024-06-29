task = input("input a task description:")
priority = input("high, medium, low?: ")
time_bound = input("is it time-bound? (yes or no): ")
match priority:
    case "high":
        if time_bound == "yes":
            print(f"{task}" " is a high priority task that requires immediate attention today!.")
match priority:
    case "low":
        if time_bound == "no":
            print(f"{task}" " is a low priority task. Consider completing it when you have free time.")
