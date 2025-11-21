def main():
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").strip().lower()
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

    match priority:
        case "high":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
            else:
                print(f"Reminder: '{task}' is a {priority} priority task. Consider scheduling it appropriately.")
        case "low":
            if time_bound == "yes":
                print(f"Note: '{task}' is a low priority task that requires immediate attention today!")
            else:
                print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
        case _:
            print(f"Note: '{task}' has an unknown priority")

if __name__ == "__main__":
    main()
