
print("Welcome to Divyansh ToDo list !!")
tasks = []

def display_tasks():
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("Your To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def add_task():
    task = input("Enter the task you want to add: ")
    tasks.append(task)
    print(f"Task '{task}' added to your to-do list.")

def update_task():
    display_tasks()
    try:
        task_index = int(input("Enter the task number you want to update: ")) - 1
        if 0 <= task_index < len(tasks):
            new_task = input("Enter the new task: ")
            tasks[task_index] = new_task
            print("Task updated successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    display_tasks()
    try:
        task_index = int(input("Enter the task number you want to delete: ")) - 1
        if 0 <= task_index < len(tasks):
            removed_task = tasks.pop(task_index)
            print(f"Task '{removed_task}' removed from your to-do list.")
        else:
            print("Task Doesnt exist!!")
    except ValueError:
        print("Please enter a valid number.")

def to_do_list_manager():
    while True:
        print("\n--- DIVYANSH LIST ---")
        print("1. Display Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            display_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            update_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Exiting the to do list !! , Goodbye!")
            break
        else:
            print("Invalid option! Please choose a number between 1 and 5.")


to_do_list_manager()
