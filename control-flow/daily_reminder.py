def main():
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").strip().lower()
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

    match priority:
        case "high":
            reminder = f"Reminder: '{task}' is a {priority} priority task"
	case "medium":
	    reminder = f"Reminder: '{task}' is a {priority} priority task"
        case "low":
            reminder = f"Note: '{task}' is a low priority task"
        case _:
            reminder = f"Note: '{task}' has an unknown priority"

    if time_bound == "yes":
        reminder += " that requires immediate attention today!"
    elif time_bound == "no" and priority == "low":
        reminder += ". Consider completing it when you have free time."
    elif time_bound == "no" and priority in ["high", "medium"]:
        reminder += ". Consider scheduling it appropriately."

    print(reminder)

if __name__ == "__main__":
    main()
