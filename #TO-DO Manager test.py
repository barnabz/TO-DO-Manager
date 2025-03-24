import datetime  


Tasks = []

def show_menu():
    print("\nTO-DO List Manager: 1.Add Tasks  2.View Tasks  3.Edit Task  4.Delete Task  5.Mark Done  6.Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        task = input("Enter a new task: ")
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")  # Get current date in YYYY-MM-DD format
        Tasks.append({"description": task, "date": current_date, "done": False})  # Add task as a dictionary
        print(f"Task '{task}' added on {current_date}!")

    elif choice == "2":
        if Tasks:
            print("\nYour Tasks: ", end="")
            for i, task in enumerate(Tasks, 1):
                status = "✓" if task["done"] else " "
                print(f"{i}. {task['description']} ({task['date']}) [{status}]", end="  ")
            print()
        else:
            print("No tasks yet!")

    elif choice == "3":  # Edit task
        if Tasks:
            print("\nYour Tasks: ", end="")
            for i, task in enumerate(Tasks, 1):
                status = "✓" if task["done"] else " "
                print(f"{i}. {task['description']} ({task['date']}) [{status}]", end="  ")
            print()
            num = int(input("Enter task number to edit: "))
            if 1 <= num <= len(Tasks):
                new_description = input("Enter new task description: ")
                Tasks[num-1]["description"] = new_description
                print(f"Task {num} updated to '{new_description}'!")
            else:
                print("Invalid number")
        else:
            print("No tasks available")

    elif choice == "4":  # Delete task
        if Tasks:
            print("\nYour Tasks: ", end="")
            for i, task in enumerate(Tasks, 1):
                status = "✓" if task["done"] else " "
                print(f"{i}. {task['description']} ({task['date']}) [{status}]", end="  ")
            print()
            num = int(input("Enter task number to delete: "))
            if 1 <= num <= len(Tasks):
                removed = Tasks.pop(num-1)
                print(f"Deleted '{removed['description']}' on {removed['date']}")
            else:
                print("Invalid number")
        else:
            print("No tasks available")

    elif choice == "5":  # Mark task as done
        if Tasks:
            print("\nYour Tasks: ", end="")
            for i, task in enumerate(Tasks, 1):
                status = "✓" if task["done"] else " "
                print(f"{i}. {task['description']} ({task['date']}) [{status}]", end="  ")
            print()
            num = int(input("Enter task number to mark as done: "))
            if 1 <= num <= len(Tasks):
                Tasks[num-1]["done"] = True
                print(f"Task '{task['description']}' marked as done!")
            else:
                print("Invalid number")
        else:
            print("No tasks available")

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!!")