def task():
    tasks = [] #empty list
    print("---- WELCOME TO THE TASK MANAGEMENT APP")

    total_task = int(input("Enter how many task you want to add: "))
    for i in range(1,total_task+1):
        task_name = input(f"Enter task {i}: ")
        tasks.append(task_name)

    print(f"Today's tasks are:\n{tasks}")

    while True:
        try:
            operation = int(input("Enter 1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/stop: "))
            if operation == 1:
                add = input("Enter task you want to add: ")
                tasks.append(add)
                print(f"Task '{add}' has been successfully added.")

            elif operation == 2:
                updated_val = input("Enter the task name you want to update: ")
                if updated_val in tasks:
                    up = input(f"Enter new task for '{updated_val}': ")
                    ind = tasks.index(updated_val)
                    tasks[ind] = up
                    print(f"Task '{updated_val}' updated to '{up}'.")
                else:
                    print(f"Task '{updated_val}' not found.")

            elif operation == 3:
                delete_val = input("Enter the task name you want to delete: ")
                if delete_val in tasks:
                    tasks.remove(delete_val)
                    print(f"Task '{delete_val}' has been successfully deleted.")
                else:
                    print(f"Task '{delete_val}' not found.")

            elif operation == 4:
                print("Today's tasks:")
                for i, task in enumerate(tasks):
                    print(f"{i+1}. {task}")

            elif operation == 5:
                print("Exiting task management app.")
                break

            else:
                print("Invalid operation. Please enter a number between 1 and 5.")

        except ValueError:
            print("Invalid input. Please enter a number.")

task()