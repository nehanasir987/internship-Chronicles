print("======= Welcome to the TO-DO List App! =======")

todo = []  # empty list to store tasks

while True:
    print("\nChoose an option:")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Remove a task")
    print("4. Search a task")
    print("5. Exit")
    
    choice = input("Enter an option (1-5): ")

    # Option 1: Add task
    if choice == "1":
        add_task = input("Enter a task: ")
        todo.append(add_task)
        print(f" Task '{add_task}' is successfully added to your To-Do List.")

    # Option 2: View all tasks
    elif choice == "2":
        if len(todo) == 0:
            print("No tasks added yet!")
        else:
            print("\nMy To-Do List:")
            for i, task in enumerate(todo, 1):  # enumerate = show number + item
                print(f"{i}. {task}")

    # Option 3: Remove a task
    elif choice == "3":
        if len(todo) == 0:
            print("⚠ No tasks to remove! Your list is already empty.")
        else:
            print("\n🗑 Your Tasks:")
            for i, task in enumerate(todo, 1):
                print(f"{i}. {task}")
            try:
                rem = int(input("Enter task number to remove: "))
                removed = todo.pop(rem - 1)  # fixed line
                print(f"🗑 Task '{removed}' removed successfully!")
            except (ValueError, IndexError):
                print("⚠ Invalid task number! Try again.")
                
    # Option 4: Search a task
    elif choice == "4":
        search_task = input("Enter a task to search: ").lower()
        matches = [task for task in todo if search_task in task.lower()]
        if matches:
            print("\nMatching tasks found:")
            for task in matches:
                print(f"- {task}")
        else:
            print("No matching tasks found.")

    # Option 5: Exit
    elif choice == "5":
        print("Thank you for using the To-Do List App!")
        break

    # Invalid input
    else:
        print("Invalid choice! Please enter a number between 1-5.")
