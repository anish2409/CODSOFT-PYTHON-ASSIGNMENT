todo_list = []

def add_task(task):
    todo_list.append(task)
    print("Task added:", task)

def remove_task(task):
    if task in todo_list:
        todo_list.remove(task)
        print("Task removed:", task)
    else:
        print("Task not found in the to-do list.")
        
def show_tasks():
    if todo_list:
        print("To-Do List:")
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")
    else:
        print("Your to-do list is empty.")
        
while True:
    print("\nOptions:")
    print("Enter 'add' to add a task")
    print("Enter 'remove' to remove a task")
    print("Enter 'show' to display your to-do list")
    print("Enter 'quit' to exit")

    user_input = input(": ")

    if user_input == "quit":
        break
    elif user_input == "add":
        task = input("Enter the task: ")
        add_task(task)
    elif user_input == "remove":
        task = input("Enter the task to remove: ")
        remove_task(task)
    elif user_input == "show":
        show_tasks()
    else:
        print("Invalid input. Please enter a valid command.")
