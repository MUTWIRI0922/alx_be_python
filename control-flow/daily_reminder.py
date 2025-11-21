def main():
    # Prompt user for input
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").strip().lower()
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

    # Process task based on priority using match-case
    match priority:
        case "high":
            reminder = f"Reminder: '{task}' is a high priority task"
        case "medium":
            reminder = f"Reminder: '{task}' is a medium priority task"
        case "low":
            reminder = f"Note: '{task}' is a low priority task"
        case _:
            reminder = f"Note: '{task}' has an unknown priority"

    # Modify reminder if time-bound
    if time_bound == "yes":
        reminder += " that requires immediate attention today!"
    elif time_bound == "no" and priority != "low":
        reminder += ". Consider scheduling it appropriately."
    elif time_bound == "no" and priority == "low":
        reminder += ". Consider completing it when you have free time."

    print(reminder)

if __name__ == "__main__":
    main()
