tasks = [] 


def add_task():
  task_description = input("Enter task description: ")
  tasks.append(task_description)
  print("Task added successfully!")


def view_tasks():
  if tasks:
    print("To-Do List:")
    for i, task in enumerate(tasks, start=1):
      print(f"{i}. {task}")
  else:
    print("Your to-do list is empty.")


def delete_task():
  view_tasks()
  if tasks:
    try:
      task_index = int(input("Enter the task number to delete: ")) - 1
      if 0 <= task_index < len(tasks):
        deleted_task = tasks.pop(task_index)
        print(f"Task '{deleted_task}' deleted successfully!")
      else:
        print("Invalid task number. Please try again.")
    except ValueError:
      print("Invalid input. Please enter a number.")
  else:
    print("Nothing to delete. Your to-do list is empty.")


while True:
  print("\nOptions:")
  print("1. Add a task")
  print("2. View tasks")
  print("3. Delete a task")
  print("4. Quit")

  choice = input("Enter your choice: ")

  if choice == "1":
    add_task()
  elif choice == "2":
    view_tasks()
  elif choice == "3":
    delete_task()
  elif choice == "4":
    print("Goodbye!")
    break
  else:
    print("Invalid choice. Please try again.")
