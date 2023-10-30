tasks = []

while True:
  print("\nOptions:")
  print("1. Add a task")
  print("2. View tasks")
  print("3. Quit")

  choice = input("Enter your choice: ")

  if choice == "1":
    task_description = input("Enter task description: ")
    tasks.append(task_description)
    print("Task added successfully!")
  elif choice == "2":
    if tasks:
      print("To-Do List:")
      for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")
    else:
      print("Your to-do list is empty.")
  elif choice == "3":
    print("Goodbye!")
    break
  else:
    print("Invalid choice. Please try again.")
